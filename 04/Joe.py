#!/usr/bin/python
__author__ = 'Mayank'


# Instance methods are variables defined in the class, accessed as instance.method()

class Joe(object):
    greeting = 'Hello, Joe!'

    # when instance method is called through an instance, the instance is automatically passed as 1st argument
    def callme(self):  # self is the instance on which the method is called.
        print 'Invoked method callme()'
        print self


this_joe = Joe()
print this_joe.greeting
this_joe.callme()
print this_joe
