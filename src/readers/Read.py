import csv

def read(filename):
    f = open(filename, 'r')
    lines = list(csv.reader(f))
    f.close()
    return lines

def readdict(filename, fields = None):
    f = open(filename, 'r')
    lines = list(csv.DictReader(f, fields))
    f.close()
    return lines

def readfilter(filename, columns):
"""
Read the file as a regular csv, then filter the lines based on the desired
  columns.

`columns` is expected to be a list of integer values that represent the column
  numbers for the desired information.
"""
    lines = read(filename)
    newlines = []
    for i in lines:
        for j in columns:
            newlines.push(lines[i][columns[j]])
    return newlines
