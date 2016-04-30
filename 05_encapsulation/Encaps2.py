#!/usr/bin/python
__author__ = 'Mayank'


class MyInteger(object):
    def set_val(self, val):
        try:
            val = int(val)
        except ValueError:
            return
        self.val = val

    def get_val(self):
        return self.val

    def increment_val(self):
        self.val = self.val + 1


myint = MyInteger()
myint.set_val(23)
print myint.get_val()
myint.increment_val()
print myint.get_val()

myint.set_val("hi")  # Exception encountered, return gracefully without doing anything
print myint.get_val()  # value not set to hi

myint.val = "hi"  # Breaking Encapsulation
print myint.get_val()
print myint.increment_val()  # Throws exception
