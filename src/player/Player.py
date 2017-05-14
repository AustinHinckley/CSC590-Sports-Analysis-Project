from base.Base import *

class Player(Base):
    '''
    All data for a player is determined here.
    '''
    def __init__(self):
        Base.__init__()

    @property
    def years(self):
        pass

    @years.setter
    def years(self, years)