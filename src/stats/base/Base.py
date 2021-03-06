from abc import ABCMeta, abstractmethod
from .Stats import Stats


class Base(metaclass=ABCMeta):  # lint:ok
    '''
    The base class for all teams and players, and defines the base API.

    Actual initialization should be done by the inheriting class(es).
    '''

    def __init__(self, _id):
        self._name = ''  # add name when looking up ID
        self._id = _id
        self._years = []
        self._stats = None  # overwrite this with a Stats object

    @property
    def stats(self):
        '''Returns the internal stats object'''
        return self._stats

    def setStats(self, lines, header=None):
        '''
        Sets the stats object for the class. Can only be called once.

        This function can be called with or without the header:
        - Calling without the header assumes that the *entire* csv file is
          provided, including the first line
        - Calling with the header assumes that the csv file is being read with
          csv.readCsvDict()
          - The first line can be successfully ignored here
        '''
        if self._stats is not None:
            return -1  # removes the need for a boolean
        else:
            idIndex = 0
            if len(self._id) == 3:
                idIndex = 3
            self._stats = Stats(lines, header, self._id, idIndex)

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id
