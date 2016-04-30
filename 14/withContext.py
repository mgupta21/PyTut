#!/usr/bin/python
__author__ = 'Mayank'


# TODO : fix error
# with 'with' enter an exit methods are called automatically, useful for initialization and clean up

class MyClass(object):
    def __enter__(self):
        print 'we have entered "with"'
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print 'we are leaving "with"'
        print('error type : {0}'.format(exc_type))
        print('error valued : {0}'.format(exc_val))
        print('error traceback : {0}'.format(exc_tb))

    def sey_hi(self):
        print 'hi, instance {0}'.format(id(self))


with MyClass as cc:
    cc.sey_hi()
    5 / 0

print 'after with'
