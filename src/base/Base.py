from abc import ABCMeta
import 'Stats'

class Base(metaclass=ABCMeta):
'''
The base class for all teams and players, and defines the base API.

Actual initialization should be done by the inheriting class(es).
'''

    def __init__(self):
        self._name = ''
        self._id = ''
        self._years = []
        self._stats = None # overwrite this with a Stats object

    @property
    def stats(self):
    '''Returns the internal stats object; good for functional-style programming'''
        return self._stats

    @stats.setter
    def stats(self, lines, header = None):
    '''
    Sets the stats object for the class. Can only be called once.

    This function can be called with or without the header:
    - Calling without the header assumes that the *entire* csv file is
      provided, including the first line
    - Calling with the header assumes that the csv file is being read with
      csv.readCsvDict()
      - The first line can be successfully ignored here
    '''
        if this._stats is not None:
            return -1 # removes the need for a boolean
        if header is not None:
            this._stats = Stats(lines, header)
        else:
            this._stats = Stats(lines)

    @property
    def name(self):
        return this._name

    @name.setter
    def name(self, name):
        this._name = name

    @property
    def id(self):
        return this._id

    @id.setter
    def id(self, id):
        this._id = id

    @property
    @abstractmethod
    def years(self):
        '''Must be implemented in inheriting class(es)'''
        pass

    @years.setter
    @abstractmethod
    def years(self, years):
        '''Must be implemented in inheriting class(es)'''
        pass
