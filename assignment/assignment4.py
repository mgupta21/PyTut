#!/usr/bin/python
__author__ = 'Mayank'

import os.path
from custom_error import MyDictError


class MyCustomDict(dict):
    def __init__(self, filename):

        self.filename = filename
        if os.path.isfile(self.filename):
            with open(self.filename, 'r') as f:
                for line in f:
                    line = line.rstrip()
                    k, v = line.split('=', 1)
                    dict.__setitem__(self, k, v)

    def __setitem__(self, key, value):

        dict.__setitem__(self, key, value)
        with open(self.filename, 'w') as f:
            for k, v in self.items():
                f.write('{0}={1}\n'.format(k, v))

    def __getitem__(self, key):
        if not key in self:
            raise MyDictError('Key : ' + key + ' not found. Available keys are :: \n' + ', '.join(self.keys()))
        return dict.__getitem__(self, key)


dd = MyCustomDict('config2.txt')
dd['x']
