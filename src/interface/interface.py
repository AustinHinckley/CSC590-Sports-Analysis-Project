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

    def __init__(self, lines, minWidth=800, minHeight=600):
        ''' Initialize root window and widgets '''
        self.root = Tk()
        self.root.minsize(width=minWidth, height=minHeight)
        self.root.title(Interface.WINDOW_TITLE)
        self.error = False
        self.errorLabel = None

        # Get values from the file that will go in dropdown menus
        self._getYearsTeamsAndPlayers(lines)

        # Build and load UI components
        self._createWidgets()
        self._loadWidgets()


    ''' Initialization methods '''

    def _getYearsTeamsAndPlayers(self, lines):
        ''' This method creates a nested dictionary and three lists
            The dictionary is for retrieving teams for certain years, etc.
            The lists are what is actually displayed in the menus'''
        self.yrsTeamsPlayers = {}    # 'Year' : { 'Team' : [players]}
        self.years = []
        teamSet = set()
        playerSet = set()
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
                    self.years.append(year)
                if team not in self.yrsTeamsPlayers[year]:
                    self.yrsTeamsPlayers[year][team] = []
                if player not in self.yrsTeamsPlayers[year][team]:
                    self.yrsTeamsPlayers[year][team].append(player)

                # Add to the initial team and players lists
                teamSet.add(team)
                playerSet.add(player)

        # Get sorted list of teams and players
        self.teams = ['All'] + sorted(teamSet)
        self.players = ['All'] + sorted(playerSet)


    def _createWidgets(self):
        ''' Initializes widgets in the root window '''
        # Start year drop down
        self.startYearVar = StringVar(self.root)
        self.startYearVar.set(self.years[0])
        self.startYearMenu = OptionMenu(self.root, self.startYearVar, *self.years,
                                command=self._changeYearTeamPlayer)
        # End year drop down
        self.endYearVar = StringVar(self.root)
        self.endYearVar.set(self.years[-1])
        self.endYearMenu = OptionMenu(self.root, self.endYearVar, *self.years,
                                        command=self._changeYearTeamPlayer)
        # Teams drop down
        self.teamVar = StringVar(self.root)
        self.teamVar.set(self.teams[0])
        self.teamMenu = OptionMenu(self.root, self.teamVar, *self.teams,
                                    command=self._changeYearTeamPlayer)
        # Players drop down
        self.playerVar = StringVar(self.root)
        self.playerVar.set(self.players[0])
        self.playerMenu = OptionMenu(self.root, self.playerVar, *self.players,
                                        command=self._changeYearTeamPlayer)

    def _loadWidgets(self):
        ''' Loads widgets into the root window to later be displayed with mainloop '''
        # Start year
        Label(self.root, text='Start Year').grid(row=1, column=1)
        self.startYearMenu.grid(row=1, column=2)

        # End year
        Label(self.root, text='End Year').grid(row=1, column=3)
        self.endYearMenu.grid(row=1, column=4)

        # Team
        Label(self.root, text='Team').grid(row=1, column=6)
        self.teamMenu.grid(row=1, column=7)

        # Players
        Label(self.root, text='Player').grid(row=1, column=9)
        self.playerMenu.grid(row=1, column=10)


    ''' Event listeners and operations for the option menus '''

    def _changeYearTeamPlayer(self, value):
        ''' A value in a dropdown was changed, so update dropdown values as needed '''
        startYear = int(self.startYearVar.get())
        endYear = int(self.endYearVar.get())
        teamChosen = self.teamVar.get()
        playerChosen = self.playerVar.get()

        if startYear > endYear:
            self._displayError('Start date cannot be larger than end date')
        else:
            self._removeError()

            # Get new years, teams, and players
            self.years = []
            teamSet = set()
            playerSet = set()
            for yrNum in range(startYear, endYear + 1):    # For each year in the given range
                year = str(yrNum)
                self.years.append(year)
                for tm in self.yrsTeamsPlayers[year]:    # For all teams for those years
                    if teamChosen == 'All' or tm == teamChosen:
                        # Only add selected team unless 'All' is selected
                        teamSet.add(tm)
                        for plr in self.yrsTeamsPlayers[year][tm]:
                            # For each player on the team in this year, only add selected
                            # unless 'All' is selected
                            if playerChosen == 'All' or plr == playerChosen:
                                playerSet.add(plr)
            self.teams = ['All'] + sorted(teamSet)
            self.players = ['All'] + sorted(playerSet)

            # Remove old lists from option menus
            self.startYearMenu['menu'].delete(0, 'end')
            self.endYearMenu['menu'].delete(0, 'end')
            self.teamMenu['menu'].delete(0, 'end')
            self.playerMenu['menu'].delete(0, 'end')

            # Set new menu lists
            for yr in self.years:
                self.startYearMenu['menu'].add_command(label=yr, command=lambda v=yr: self.startYearVar.set(v))
                self.endYearMenu['menu'].add_command(label=yr, command=lambda v=yr: self.endYearVar.set(v))
            for tm in self.teams:
                self.teamMenu['menu'].add_command(label=tm, command=lambda v=tm: self.teamVar.set(v))
            for plr in self.players:
                self.playerMenu['menu'].add_command(label=plr, command=lambda v=plr: self.playerVar.set(v))


    ''' Plot/display/misc. functions '''

    def _displayError(self, text):
        ''' Shows error message underneath the widgets '''
        self.error = True
        self.errorLabel = Label(self.root, text=text, fg='red')

    def _removeError(self):
        ''' Removes error message from the grid '''
        if (self.error): self.errorLabel.grid_forget()

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
