#!/usr/bin/python
__author__ = 'Mayank'

import pickle


class MyClass(object):
    def __init__(self, val):
        self.value = val

    def increment(self):
        self.value += 1


obj = MyClass(9)
obj.increment()
obj.increment()

filename = 'datafile_.txt'
with open(filename, 'w') as f:
    pickle.dump(obj, f)

with open(filename) as f:
    un_pickled_obj = pickle.load(f)

print un_pickled_obj
print un_pickled_obj.value
