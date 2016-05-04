#!/usr/bin/python
__author__ = 'Mayank'

import os.path


class MyDictError(KeyError):
    def __init__(self, this, key):
        self.key = key
        self.keys = this.keys()

    def __str__(self):
        return 'key "{0}" not found. Available keys : "{1}"'.format(self.key, ', '.join(self.keys))


class MyCustomDict(dict):
    def __init__(self, filename):
        self._filename = filename
        if not os.path.isfile(self._filename):
            try:
                open(self._filename, 'w').close()
            except IOError:
                raise IOError('arg to MyCustomDic must be a valid path name')
        with open(self._filename, 'r') as f:
            for line in f:
                line = line.rstrip()
                k, v = line.split('=', 1)
                dict.__setitem__(self, k, v)

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        with open(self._filename, 'w') as f:
            for k, v in self.items():
                f.write('{0}={1}\n'.format(k, v))

    def __getitem__(self, key):
        if not key in self:
            raise MyDictError(self, key)
        return dict.__getitem__(self, key)
