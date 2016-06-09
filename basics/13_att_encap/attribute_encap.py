#!/usr/bin/python
__author__ = 'Mayank'


# python doesn't enforce privatization
# @property is a decorator that an instance attributes as encapsulate-able through methods
# The names linked to attributes names must be used by methods, setter and deleter


class GetSet(object):
    def __init__(self, value):
        self.attValue = value

    @property
    def var(self):
        print 'Retrieving the saved "var" attribute'
        return self.attValue

    @var.setter
    def var(self, value):
        print 'setting the "var" attribute'
        self.attValue = value

    @var.deleter
    def var(self):
        print 'deleting the "var" attribute'
        self.attValue = None


obj = GetSet(10)

print obj.var
obj.var = 50
print obj.var
del obj.var
print obj.var

# Below still works
obj.attValue = 70
print obj.attValue
