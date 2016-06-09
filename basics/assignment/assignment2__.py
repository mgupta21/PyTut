#!/usr/bin/python
__author__ = 'Mayank'

from datetime import datetime


class Writer(object):
    def __init__(self, filename, formatter):
        self.formatter = formatter()
        self.fh = open(filename, 'w')

    def write(self, txt):
        self.fh.write(self.formatter.format(txt) + '\n')

    def close(self):
        self.fh.close()


class CSVFormatter(object):
    def __init__(self):
        self.delim = ','

    def format(self, list):
        temp_list = []
        for element in list:
            if self.delim in element:
                temp_list.append('"{0}"'.format(element))
            else:
                temp_list.append(element)
        return self.delim.join(temp_list)


class LogFormatter(object):
    def format(self, txt):
        dt = datetime.now().strftime('%Y-%m-%d %H:%M')
        return '{0}     {1}'.format(dt, txt)
