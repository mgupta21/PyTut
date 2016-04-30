#!/usr/bin/python
__author__ = 'Mayank'

from assignment2__ import Writer, CSVFormatter, LogFormatter

csvWriter = Writer('mycsv.csv', CSVFormatter)
csvWriter.write(['sa', 're', 'ga', 'ma', 'pa'])
csvWriter.write(['A', 'E', 'I', 'O', 'U'])
csvWriter.write(['a', 'b,2', 'c', 'd,4', 'e'])
csvWriter.close()

logWriter = Writer('mylog.txt', LogFormatter)
logWriter.write('first log message')
logWriter.write('second log message')
logWriter.close()
