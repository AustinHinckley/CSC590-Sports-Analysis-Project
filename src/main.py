'''
CSC 590 Group 1 Final Project
Date: May 15, 2017
Team Members:
    1) James Hibben
    2) Joosung Lee
    3) Darren Williams
    4) Austin Hinckley
    5) Joshua Yamdogo

This file gets data from a CSV file and initializes the user-interface.

*** NOTE: If the program crashes, try reinstalling matplotlib with pip: ***
    pip uninstall matplotlib
    pip install matplotlib
'''
from readers.Read import *
from interface.interface import *

def main():
    lines = read("Batting.csv")
    UI = Interface(lines=lines)
    UI.display()

if __name__ == '__main__':
    main()
