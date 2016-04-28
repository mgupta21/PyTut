#!/usr/bin/python
__author__ = 'Mayank'


class MyClass(object):
    pass  # Used to represent no context in python


class MyClass2(object):
    var = 10


this_obj = MyClass()
print this_obj

that_obj = MyClass()
print that_obj

this_obj2 = MyClass2()
print this_obj2.var
