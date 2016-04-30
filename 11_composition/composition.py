#!/usr/bin/python
__author__ = 'Mayank'

import StringIO


class WriteMyStuff(object):
    def __init__(self, writer):
        self.writer = writer

    def write(self):
        self.writer.write("this is a silly message")  # calls write on object passed


fh = open('test.txt', 'w')
w1 = WriteMyStuff(fh)
w1.write()
fh.close()

sioh = StringIO.StringIO()
w2 = WriteMyStuff(sioh)
w2.write()

print 'file object : ', open('test.txt', 'r').read()
print 'StringIO object : ', sioh.getvalue()
