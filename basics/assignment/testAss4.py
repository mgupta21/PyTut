#!/usr/bin/python
__author__ = 'Mayank'

"""
    Usages :
    ./testAss4.py                       (display entire dict)
    ./testAss4.py <key>                 (print's the value associated with the key)
    ./testAss4.py <key> <value>         (sets given key and value in the dict)
"""

import sys
from assignment4 import MyCustomDict

d = MyCustomDict('rev_analysis.txt')
if len(sys.argv) == 3:
    key = sys.argv[1]
    value = sys.argv[2]
    print('setting key "{0}" and value "{1}" in dictionary'.format(key, value))
    d[key] = value

elif len(sys.argv) == 2:
    print('reading a value from dictionary')
    key = sys.argv[1]
    print('the value for key "{0}" is : "{1}"'.format(key, d[key]))

else:
    print("Displaying dictionary : ")
    for key in d.keys():
        print("{0} = {1}".format(key, d[key]))
