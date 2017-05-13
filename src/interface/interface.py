import tkinter as Tk
from tkinter import *
import matplotlib.pyplot as plt
from IPython.display import display

# Putting these here because we might need them
import matplotlib
#matplotlib.user('TkAgg')
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

pidx, yrx, teamx = 0, 1, 3

class Interface:
    ''' This class will contain the Tkinter objects and various UI-related methods '''
    WINDOW_TITLE = "Baseball Plot GUI"

    def __init__(self, lines=None, minWidth=800, minHeight=600):
        ''' Initialize window and user widgets '''
        self.root = Tk()
        self.root.minsize(width=minWidth, height=minHeight)
        self.root.title(Interface.WINDOW_TITLE)

        # Get values from the file that will go in dropdown menus
        self.yrsTeamsPlayers = {}    # 'Year' : { 'Team' : [players]}
        self.years = []
        if lines is not None:
            # Go through all lines and add years, teams, and players
            for row in lines[1:]:
                year = row[yrx]
                team = row[teamx]
                player = row[pidx]
                if int(year) < 1950:
                    continue

                # Add year, team, and player as necessary
                if year not in self.yrsTeamsPlayers:
                    self.yrsTeamsPlayers[year] = {}
                if team not in self.yrsTeamsPlayers[year]:
                    self.yrsTeamsPlayers[year][team] = []
                if player not in self.yrsTeamsPlayers[year][team]:
                    self.yrsTeamsPlayers[year][team].append(player)
            self.years = list(self.yrsTeamsPlayers.keys())
        # End result: nested dictionary for players on all teams for all years

        self._createWidgets()

    def _createWidgets(self):
        ''' Initializes widgets in the root window '''
        # Start year drop down
        self.startYearVar = StringVar(self.root)
        self.startYearVar.set(self.years[0])
        self.startYearMenu = OptionMenu(self.root, self.startYearVar, *self.years)

        # End year drop down
        self.endYearVar = StringVar(self.root)
        self.endYearVar.set(self.years[-1])
        self.endYearMenu = OptionMenu(self.root, self.endYearVar, *self.years)

        self._loadWidgets()

    def _loadWidgets(self):
        ''' Loads widgets into the root window to later be displayed with mainloop '''
        Label(self.root, text='Start Year').grid(row=1, column=1)
        self.startYearMenu.grid(row=1, column=2)
        Label(self.root, text='End Year').grid(row=1, column=3)
        self.endYearMenu.grid(row=1, column=4)


    # Should somehow include event listeners? Maybe?

    def createPlot(self, dataX, dataY, markerStyle, markerColor):
        ''' Builds a plot from the given data and adds it to the window '''
        # Can maybe use canvas = FigureCanvasTkAgg(<Figure>, master=window)
        # Then do something like canvas.get_tk_widget().pack(...) or canvas._tkcanvas.pack(...)
        pass

    def display(self):
        ''' Calls mainloop() to show the window '''
        self.root.mainloop()

    def close(self):
        ''' Closes the interface window and destroys it '''
        self.root.quit()
        self.root.destroy()
