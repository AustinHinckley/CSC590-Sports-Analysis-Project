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
    STATS = ['G','AB','R','H','2B','3B','HR','RBI','SB','CS','BB','SO','HBP','GIDP']

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

                # Add to the team set to get unique teams
                teamSet.add(team)

        # Get sorted list of teams and players
        self.teams = ['All'] + sorted(teamSet)
        self.players = ['All']


    def _createWidgets(self):
        ''' Initializes widgets in the root window (with listeners to _changeYearTeamPlayer) '''
        # Start year drop down
        self.startYearVar = StringVar(self.root)
        self.startYearVar.set(self.years[0])
        self.startYearMenu = OptionMenu(self.root, self.startYearVar, *self.years)
        self.startYearVar.trace('w', self._changeYearTeamPlayer)

        # End year drop down
        self.endYearVar = StringVar(self.root)
        self.endYearVar.set(self.years[-1])
        self.endYearMenu = OptionMenu(self.root, self.endYearVar, *self.years)
        self.endYearVar.trace('w', self._changeYearTeamPlayer)

        # Teams drop down
        self.teamVar = StringVar(self.root)
        self.teamVar.set(self.teams[0])
        self.teamMenu = OptionMenu(self.root, self.teamVar, *self.teams)
        self.teamVar.trace('w', self._changeYearTeamPlayer)

        # Players drop down
        self.playerVar = StringVar(self.root)
        self.playerVar.set(self.players[0])
        self.playerMenu = OptionMenu(self.root, self.playerVar, *self.players)
        self.playerVar.trace('w', self._changeYearTeamPlayer)

        # Stat X drop down
        self.xStatVar = StringVar(self.root)
        self.xStatVar.set(Interface.STATS[0])
        self.xStatMenu = OptionMenu(self.root, self.xStatVar, *Interface.STATS)

        # Stat Y drop down
        self.yStatVar = StringVar(self.root)
        self.yStatVar.set(Interface.STATS[1])
        self.yStatMenu = OptionMenu(self.root, self.yStatVar, *Interface.STATS)


    def _loadWidgets(self):
        ''' Loads widgets into the root window to later be displayed with mainloop '''
        # Start year
        Label(self.root, text='Start Year').grid(row=1, column=1, sticky=E)
        self.startYearMenu.grid(row=1, column=2, sticky=W)

        # End year
        Label(self.root, text='End Year').grid(row=2, column=1, sticky=E)
        self.endYearMenu.grid(row=2, column=2, sticky=W)

        # Team
        Label(self.root, text='Team').grid(row=3, column=1, sticky=E)
        self.teamMenu.grid(row=3, column=2, sticky=W)

        # Players
        Label(self.root, text='Player').grid(row=4, column=1, sticky=E)
        self.playerMenu.grid(row=4, column=2, sticky=W)

        # Spacer (empty space between columns)
        Label(self.root, text='').grid(row=1, column=3, padx=20)

        # Stat X
        Label(self.root, text='X-Axis').grid(row=1, column=4, sticky=E)
        self.xStatMenu.grid(row=1, column=5, sticky=W)

        # Stat Y
        Label(self.root, text='Y-Axis').grid(row=2, column=4, sticky=E)
        self.yStatMenu.grid(row=2, column=5, sticky=W)


    ''' Event listeners and operations for the option menus '''

    def _changeYearTeamPlayer(self, *args):
        ''' A value in a dropdown was changed, so update dropdown values as needed '''
        startYear = int(self.startYearVar.get())
        endYear = int(self.endYearVar.get())
        teamChosen = self.teamVar.get()
        playerChosen = self.playerVar.get()

        if startYear > endYear:
            self._displayError('Start date cannot be larger than end date')
        else:
            self._removeError()

            # Get teams and players that existed in the date range
            teamSet = set()
            playerSet = set()
            for yrNum in range(startYear, endYear + 1):    # For each year in the given range
                year = str(yrNum)
                for tm in self.yrsTeamsPlayers[year]:    # For all teams for those years
                    teamSet.add(tm)    # Always add all teams
                    if teamChosen != 'All' and teamChosen == tm:
                        # Only add players on the chosen team
                        # If 'All' is selected for team, don't add any players
                        for plr in self.yrsTeamsPlayers[year][tm]:
                            playerSet.add(plr)
            self.teams = ['All'] + sorted(teamSet)
            self.players = ['All'] + sorted(playerSet)

            # Get list of valid years for the selected team/playerSet
            self.years = []
            if teamChosen == 'All' and playerChosen == 'All':
                # Show all years in the dropdown if 'All' chosen for everything
                self.years = list(self.yrsTeamsPlayers.keys())
            elif teamChosen == 'All':
                # Just player chosen, so do nothing because we aren't going to
                # support player data without having a given team
                pass
            elif playerChosen == 'All':
                # Just the team chosen, so show all active years for that team
                for yr in self.yrsTeamsPlayers:
                    if teamChosen in self.yrsTeamsPlayers[yr]:
                        self.years.append(yr)
            else:
                # Both team and player chosen, so just show all years the player
                # played on that team
                for yr in self.yrsTeamsPlayers:
                    if teamChosen in self.yrsTeamsPlayers[yr] \
                        and playerChosen in self.yrsTeamsPlayers[yr][teamChosen]:
                        self.years.append(yr)

            # Make sure something is in years
            if len(self.years) == 0:
                self.years = list(self.yrsTeamsPlayers.keys())

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

            # Check for value conflicts and notify the user if necessary
            if startYear < int(self.years[0]):
                self._displayError('Please change start year')
            elif endYear > int(self.years[-1]):
                self._displayError('Please change end year')
            elif teamChosen not in self.teams:
                self._displayError('Please change team selection')
            elif playerChosen not in self.players:
                self._displayError('Please change player selection')

    ''' Plot/display/misc. functions '''

    def _displayError(self, text):
        ''' Shows error message underneath the widgets '''
        self.error = True
        self.errorLabel = Label(self.root, text=text, fg='red')
        self.errorLabel.grid(row=3, column=1, columnspan=10, sticky=W)

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
