'''
Contains code for
'''

# Code for generic relative imports
import os
import sys
import inspect
# realpath() will make your script run, even if you symlink it :)
cmd_folder = os.path.realpath(
    os.path.abspath(
        os.path.split(
            inspect.getfile(
                inspect.currentframe()
            )
        )[0])
    )
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

# use this if you want to include modules from a subfolder
cmd_subfolder = os.path.realpath(
    os.path.abspath(
        os.path.join(
            os.path.split(
                inspect.getfile(
                    inspect.currentframe()
                )
            )[0], "subfolder")
        )
    )
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)

# Info:
# cmd_folder = os.path.dirname(os.path.abspath(__file__))
    # DO NOT USE __file__ !!!
# __file__ fails if script is called in different ways on Windows
# __file__ fails if someone does os.chdir() before
# sys.argv[0] also fails because it doesn't always contains the path

# End relative imports

from base.Base import Base


class Team(Base):

    def __init__(self, _id):
        super().__init__(_id)

    def getStats(self, stat, years):
        '''Get a stat from a particular year or set of years
           If year is a list of years, it will iterate through
            the entire list
           Returns a String or List of Strings
        '''
        ans = []
        if isinstance(years, int):
            # convert it to a list
            year = [] + year
        for yr in year:
            ans += [self._stats.getStatFromYear(year[yr], stat)]
        if len(ans) == 1:
            return ans[0]
        return ans

    def getStatList(self, stat):
        ans = []
        return ans
        '''Get a list containing the given stat for all years'''

team = Team('tst')
# team.stats = 'test'
print((team.stats))
