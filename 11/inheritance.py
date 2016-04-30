#!/usr/bin/python
__author__ = 'Mayank'

import time


class Date(object):
    def get_date(self):
        return time.strftime("%m/%d/%y")


class Time(Date):
    def get_time(self):
        return time.strftime("%X")


obj_date = Date()
obj_time = Time()

print 'Parent class Date ::'
print obj_date.get_date()

print 'Subclass Time ::'
print obj_time.get_date()
print obj_time.get_time()
