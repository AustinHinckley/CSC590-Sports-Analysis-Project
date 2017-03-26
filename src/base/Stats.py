class Stats:
'''
Class for storing and getting statistics
All stats will be stored by year, allowing for a more straightforward and
    unified experience for retrieval.
The general form for the statistics will be:
    Year
    -> Stats
'''

    def __init__(self):
        '''Base init method - do not call directly'''
        self._stats = {}

    def __init__(self, lines):
        '''
        Actual init method -
        Pass ALL lines to this method, including the first.
        '''
        self.__init__()
        # write

    def __init__(self, lines, header):
        '''
        Actual init method
        Checks if all lines are passed and ignores the first line if necessary.
        '''
        self.__init__()

    def getYearStats(self, year):
        return self._stats[year]

    def getStatFromYear(self, year, stat):
        return self._stats[year][stat]
