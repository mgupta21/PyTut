#!/usr/bin/python
__author__ = 'Mayank'

import sys

try:
    arg = sys.argv[1]
    num = int(arg)

except (IndexError, ValueError):
    print('please pass integer as argument')

print('thanks for the int')
