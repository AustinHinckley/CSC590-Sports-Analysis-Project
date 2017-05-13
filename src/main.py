''' Main program -- this will import all classes, initialize the interface, etc.
    It may do more depending on how much functionality is implemented elsewhere.
'''
from readers.Read import *
from stats.base.Base import *
from stats.base.Stats import *
from interface.interface import *

def main():
    lines = read("Batting.csv")

    # Initialize interface
    UI = Interface(lines=lines)
    UI.display()


    '''stats = Stats(lines, id='pujolal01', idIndex=0)
    print(stats.getStatForAllYears('HR'))
    print(stats.getStatFromYear(2014, 'HR'))'''


if __name__ == '__main__':
    main()
