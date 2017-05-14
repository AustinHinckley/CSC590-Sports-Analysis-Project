from base import *

'''
note: I copied Jame's code from the Team class and
changed the class name since the functionallity is
basically the same.
'''

class Player(Base):

    def __init__(self, _id):
        super().__init__(_id)

    def getStatFromYearRange(self, stat, years):
        '''Get a stat from a particular year or set of years
           If year is a list of years, it will iterate through
            the entire list
           Returns List of Strings, even if there is only one element
        '''
        ans = []
        if isinstance(years, int):
            # convert it to a list
            years = list(years)
        for yr in years:
            # dev guard to prevent unnecessary TypeErrors
            if self._stats is not None:
                ans.append(self._stats.getStatFromYear(years[yr], stat))
        return ans

    def getStatFromAllYears(self, stat):
        '''Get a list containing the given stat for all years'''
        return self.getStats(stat, self._stats.getYearsActive())
        