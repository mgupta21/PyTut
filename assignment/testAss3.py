#!/usr/bin/python
__author__ = 'Mayank'

"""
    Usages :
    ./testAss.py                    (reads out entire dic)
    ./testAss.py <key> <value>      (sets the key and value in dic)
"""

import sys
from assignment3 import MyCustomDict as DCT

d = DCT('config_file.txt')

if len(sys.argv) == 3:
    key = sys.argv[1]
    value = sys.argv[2]
    print('Writing data : {0} = {1}'.format(key, value))
    d[key] = value
else:
    print('Reading dictionary ::')
    for key in d.keys():
        print(' {0} = {1}'.format(key, d[key]))
