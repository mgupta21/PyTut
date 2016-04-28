#!/usr/bin/python

# Everything is an Object, even numbers. There are no primitives
# Every object has a type. The object has attributes, some of which are methods

myint = 5;
mystr = 'hello';
mybol = True
mynone = None
mylist = ['a', 'b', 'c']

def func():
    print 'hello'

myfunc = func()
this_type = type(myint)

print type(myint)
print type(mystr)
print type(mybol)
print type(mynone)
print type(mylist)
print type(myfunc)
print type(this_type)

# attributes associated with an integer
print dir(myint)