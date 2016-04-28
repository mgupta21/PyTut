#!/usr/bin/python
__author__ = 'Mayank'

# Everything is an Object, even numbers. There are no primitives
# Every object has a type. The object has attributes, some of which are methods

myint = 5;
mystr = 'hello';
mybol = True
mynone = None
mylist = ['a', 'b', 'c']

def myfunc():
    print 'hello'

this_type = type(myint)

print type(myint)
print type(mystr)
print type(mybol)
print type(mynone)
print type(mylist)
print type(myfunc)
print type(this_type)

# Attributes associated with an integer
print dir(myint)