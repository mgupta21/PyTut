#!/usr/bin/python
__author__ = 'Mayank'


class MyError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('calling str')
        if self.message:
            return 'MyError exception with given message : {0}'.format(self.message)
        else:
            return 'MyError exception!'


# raise MyError
raise MyError('We have a problem!')
