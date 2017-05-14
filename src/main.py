''' Main program -- this will import all classes, initialize the interface, etc.
    It may do more depending on how much functionality is implemented elsewhere.
'''
from readers.Read import *
from stats.base.Base import *
from stats.base.Stats import *
from interface.interface import *

def main():
    lines = read("Batting.csv")
    UI = Interface(lines=lines)
    UI.display()

if __name__ == '__main__':
    main()
