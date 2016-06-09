#!/usr/bin/python
__author__ = 'Mayank'

import sys


def doubleit(x):
    if not isinstance(x, (int, float)):
        raise TypeError('Invalid argument, arg type must be integer or float')
    var = x * 2
    print var
    return var


def double_file_vals(filename):
    with open(filename) as f:
        double_list = [str(doubleit(int(val))) for val in f]
    with open(filename, 'w') as f:
        f.write('\n'.join(double_list))


if __name__ == '__main__':
    input_val = int(sys.argv[1])
    double_val = doubleit(input_val)
    print('The doubled value of {0} is {1}'.format(input_val, double_val))
