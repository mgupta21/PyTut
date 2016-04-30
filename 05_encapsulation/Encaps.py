#!/usr/bin/python
__author__ = 'Mayank'


# Although normally set in a setter method, instance attribute values can be set anywhere
# Encapsulation in python is a voluntary restriction
# Python does not implement data hiding, as does java

class MyClass(object):
    def set_val(self, val):
        self.val = val

    def get_val(self):
        return self.val


a = MyClass()
b = MyClass()

a.set_val(9)
b.set_val(65)

a.val = "Breaking Encapsulation"

print a.val
print b.val
