#!/usr/bin/python
__author__ = 'Mayank'


class MyDictError(KeyError):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = ''

    def __str__(self):
        if self.message:
            return self.message
        else:
            return 'MyDicError : Requested key not found'
