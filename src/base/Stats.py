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
        '''Base init method'''
        self._stats = {}
        self._average_stats = {}

    def __init__(self, lines):
        '''
        Actual init method. Use this one with csv.readcsv()
        Pass ALL lines to this method, including the first.
        '''
        self.__init__()
        # write

    def __init__(self, header, lines):
        '''
        Actual init method. Use this one with csv.readCsvDict()
        We will check if all lines are passed and ignore the first line.
        '''
        self.__init__()
        #

    def getYearStats(self, year):
        return self._stats[year]

    def getStatFromYear(self, year, stat):
        return self._stats[year][stat]

    def getAverageStats(self):
        return self._average_stats
