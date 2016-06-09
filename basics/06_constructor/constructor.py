#!/usr/bin/python
__author__ = 'Mayank'


# __init__ method is automatically called when a new instance is constructed

class MyNum(object):
    def __init__(self, value):
        print "calling __int__"
        try:
            value = int(value)
        except ValueError:
            value = 0
        self.val = value

    def increment(self):
        self.val += 1


dd = MyNum(3)
dd.increment()
dd.increment()
print dd.val

aa = MyNum('hi')
aa.increment()
aa.increment()
print aa.val
