#!/usr/bin/python
__author__ = 'Mayank'

import timeit

print 'By Index:    ', timeit.timeit(stmt="mydict['c']", setup="mydict = {'a':1, 'b':6, 'c':7}", number=1000000)
print 'By get:    ', timeit.timeit(stmt="mydict.get('c')", setup="mydict = {'a':1, 'b':6, 'c':7}", number=1000000)
