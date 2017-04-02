class Stats:
    '''
    Class for storing and getting statistics
    All stats will be stored by year, allowing for a more straightforward and
        unified experience for retrieval.
    The general form for the statistics will be:
        Year
        -> Stat
            -> Total number for the stat in that year (across all teams and players)
    '''

    def __init__(self, lines, header = None):
        '''
        Initialize stats object and populate data from lines
        Use header for stat names. If no header given, use first line in lines
        '''
        self._stats = {}
        yearx = 1    # This seems constant across files, but we could parse header if needed
        if header is None:
            header = lines[0]

        # Parse lines to get stats by year
        for row in lines[1:]:
            # Add year to dict if needed
            year = int(row[yearx])
            if year not in self._stats:
                self._stats[year] = {}

            # Add stat info for the row
            for i in range(0, len(row)):
                if i != yearx and row[i].isdigit():
                    # Only add data that is a number and not a year
                    stat = header[i]
                    if stat not in self._stats[year]:
                        self._stats[year][stat] = 0
                    self._stats[year][stat] += int(row[i])

    def getYearStats(self, year):
        return self._stats[year]

    def getStatFromYear(self, year, stat):
        return self._stats[year][stat]
