#!/usr/bin/python
__author__ = 'Mayank'

from assignment2 import LogFile, DelimFile

l = LogFile('log.txt')
l.write("dummy log message")

d = DelimFile('test.csv', ',')
d.write(['a', 'b', 'c', 'd'])
d.write(['1', "2", '3', '4'])
