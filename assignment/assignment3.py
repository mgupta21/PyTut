#!/usr/bin/python
__author__ = 'Mayank'

import os.path


class MyDict(dict):
    def __init__(self, filename):
        self.filename = filename

    def __setitem__(self, key, value):
        if os.path.isfile(self.filename):
            with open(self.filename, 'r+') as f:
                lines = f.readlines()
                f.truncate()
                if len(lines) != 0:
                    for line in lines:
                        k, v = line.split('=', 1)
                        if key == k:
                            f.write(key + '=' + value + '\n')
                        else:
                            f.write(k + '=' + v + '\n')
                else:
                    f.write(key + '=' + value + '\n')

        else:
            fh = open(self.filename, 'a')
            fh.write(key + '=' + value + '\n')
            fh.close()


mydict = MyDict('config.txt')
mydict['mayank'] = 'gupta'
mydict['karan'] = 'kapoor'
mydict['mayank'] = 'grover'
