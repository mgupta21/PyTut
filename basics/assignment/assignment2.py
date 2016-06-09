#!/usr/bin/python
__author__ = 'Mayank'

from datetime import datetime


class Writer(object):
    def __init__(self, filename):
        self.filename = filename

    def write_line(self, txt):
        fh = open(self.filename, 'a')
        fh.write(txt + '\n')
        fh.close()


class LogFile(Writer):
    def __init__(self, filename):
        super(LogFile, self).__init__(filename)

    def write(self, txt):
        dt = datetime.now()
        dtstr = dt.strftime('%Y-%m-%d %H:%M')
        super(LogFile, self).write_line('{0}     {1}'.format(dtstr, txt))


class DelimFile(Writer):
    def __init__(self, filename, delimiter):
        super(DelimFile, self).__init__(filename)
        self.delimiter = delimiter

    def write(self, txt):
        txt = self.delimiter.join(txt)
        super(DelimFile, self).write_line(txt)
