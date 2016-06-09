#!/usr/bin/python
__author__ = 'Mayank'


# An instance of a class knows what class it's from
# Vars/Attributes defined in the class are available to the instance
# A method  on an instance passes instance as first argument to the method
# Instance have their own data called instance attribute
# Variables defined in the class are class attributes
# When reading an attribute python looks first in instance and then in class

class MyClass(object):
    classy = 'class val'

    def set_val(self):
        self.insty = 100


dd = MyClass()
dd.set_val()

print dd.classy
print dd.insty

dd.classy = 'instance val'
print dd.classy

del dd.classy
print dd.classy
