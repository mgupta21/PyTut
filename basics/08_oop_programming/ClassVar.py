#!/usr/bin/python
__author__ = 'Mayank'


# Attributes are defined in class when they are required to be shared among all instances

class InstanceCounter(object):
    count = 0

    def __init__(self, val):
        self.val = val
        InstanceCounter.count += 1

    def get_val(self):
        return self.val

    def get_count(self):
        return InstanceCounter.count


objA = InstanceCounter(32)
objB = InstanceCounter(53)
objC = InstanceCounter(21)

for obj in (objA, objB, objC):
    print "Value of Object Instance is : %s" % obj.get_val()
    print "Instance counter is : %s " % obj.get_count()
