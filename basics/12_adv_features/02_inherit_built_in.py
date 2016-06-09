#!/usr/bin/python
__author__ = 'Mayank'


# Python lets classes inherit from build-in classes
# Inherited class can customize built-in behaviour

class MyDict(dict):
    def __setitem__(self, key, value):
        if not isinstance(value, int):
            ValueError
        # self[key] = value # RuntimeError maximum recursion depth exceeded
        dict.__setitem__(self, key, value * 100)


dd = MyDict()
dd['a'] = 3
dd['b'] = 5

for key in dd.keys():
    print '{0} = {1}'.format(key, dd[key])
