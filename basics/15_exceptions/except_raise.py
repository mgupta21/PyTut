#!/usr/bin/python
__author__ = 'Mayank'


def make_delim_line(list, delim):
    try:
        formatted_line = delim.join(list)
    except TypeError:
        raise TypeError('first argument must be a list or tuple')
    return formatted_line


fline = make_delim_line(100, ',')
