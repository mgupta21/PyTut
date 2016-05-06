#!/usr/bin/python
__author__ = 'Mayank'

import pdb


def doubleVal(mysum, val):
    # mysum = 0
    newsum = mysum + val
    return newsum


pdb.set_trace()

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mysum = 0

for val in values:
    mysum = doubleVal(mysum, val)

print mysum

# pdb commands
# l : shows current debug location in code
# n : moves debugger to next line
# s : steps into a code block
# h : lists the list of commands available
