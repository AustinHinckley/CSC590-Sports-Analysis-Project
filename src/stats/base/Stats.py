class Stats:
    '''
    Class for storing and getting statistics
    All stats will be stored by year, allowing for a more straightforward and
        unified experience for retrieval.
    The general form for the statistics will be:
        Year
        -> Stat
            -> Total number for the stat in that year
    '''

    def __init__(self, lines, header=None, id=None, idIndex=None):
        '''
        Initialize stats object and populate data from lines
        Use header for stat names. If no header given, use first line in lines

        The id is the team or player id string used to filter results
        The id index is the integer index of the id column used to filter results

        Examples:
            Stats(lines, None, 'pujolal01', 0) -- Gets stats for Albert Pujols (filter is player ID)
            Stats(lines, None, 'SLN', 3) -- Gets stats for St. Louis (filter is teamID)
        '''
        self._stats = {}
        # This seems constant across files, but we could parse header if needed
        yearx = 1
        if header is None:
            header = lines[0]

        # Parse lines to get stats by year
        for row in lines[1:]:
            if id is not None and idIndex is not None and row[idIndex] != id:
                continue    # Skip rows that don't match the given ID

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

    # TODO: finish this function
    def getYearStats(self, stat):
        years = self.getYearsActive()
        statPerYear = []
        for yr in years:
            print(yr)

    def getStatFromYear(self, year, stat):
        return self._stats[year][stat]

    def getYearsActive(self):
        return list(self._stats.keys())
