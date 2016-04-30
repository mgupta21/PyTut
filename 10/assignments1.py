#!/usr/bin/python
__author__ = 'Mayank'


class MaxSizeList(object):
    def __init__(self, max_size):
        self.max_size = max_size
        self.list = []

    def add_to_list(self, obj):
        self.list.append(obj)
        if len(self.list) > self.max_size:
            self.list.pop(0)

    def get_list(self):
        print self.list
