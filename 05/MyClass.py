#!/usr/bin/python
__author__ = 'Mayank'

# An instance can not only access class variables but also get and set values on itself, these values are called as state

import random


class MyClass():
    def dothis(self):
        self.rand_val = random.randint(1, 100)  # value is assigned to instance variable and not class variable


this = MyClass()
this.dothis()
print this.rand_val
