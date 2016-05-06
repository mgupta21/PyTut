#!/usr/bin/python
__author__ = 'Mayank'

import os.path
import pickle


class MyDictError(KeyError):
    def __init__(self, this, key):
        self.key = key
        self.keys = this.keys()

    def __str__(self):
        return 'key "{0}" not found. Available keys : "{1}"'.format(self.key, ', '.join(self.keys))


class MyCustomDict(dict):
    config_dir = ''

    def __init__(self, filename):
        self._filename = os.path.join(MyCustomDict.config_dir, filename + '.pickle')
        if not os.path.isfile(self._filename):
            with open(self._filename, 'w') as f:
                pickle.dump({}, f)
        with open(self._filename) as f:
            pkl = pickle.load(f)
            self.update(pkl)

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        with open(self._filename, 'w') as f:
            pickle.dump(self, f)

    def __getitem__(self, key):
        if not key in self:
            raise MyDictError(self, key)
        return dict.__getitem__(self, key)


c = MyCustomDict('pickle_dict')
c['a'] = 1
c['b'] = 2

for key in c.keys():
    print('{0} = {1}'.format(key, c[key]))
