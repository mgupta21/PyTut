#!/usr/bin/python
__author__ = 'Mayank'

import yaml


class MyClass(object):
    def __init__(self, val):
        self.value = val

    def increment(self):
        self.value += 1


obj = MyClass(9)
obj.increment()
obj.increment()

filename = 'yml.yaml'

with open(filename, 'w') as f:
    yaml.dump(obj, f)

with open(filename) as f:
    obj_loaded = yaml.load(f)

print obj_loaded.value
