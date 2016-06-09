#!/usr/bin/python
__author__ = 'Mayank'

import os.path


# Approach 1
class MyDict(object):
    def __init__(self, filename):
        self.filename = filename

    def __setitem__(self, key, value):
        lines_to_write = []
        is_existing = False

        if os.path.isfile(self.filename):
            with open(self.filename, 'r') as f:
                for line in f:
                    line = line.rstrip('\n')
                    k, v = line.split('=', 1)
                    if key != k:
                        lines_to_write.append('{0}={1}\n'.format(k, v))
                    elif key == k:
                        is_existing = True
                        lines_to_write.append('{0}={1}\n'.format(key, value))

        if not is_existing:
            lines_to_write.append('{0}={1}\n'.format(key, value))

        with open(self.filename, 'w') as f:
            for line in lines_to_write:
                f.write(line)

    def __getitem__(self, key):

        with open(self.filename, 'r') as f:
            for line in f:
                line = line.rstrip('\n')
                k, v = line.split('=', 1)
                if k == key:
                    return v

        return None


# Approach 2
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
