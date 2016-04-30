#!/usr/bin/python
__author__ = 'Mayank'

import abc


class GetterSetter(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, val):
        self.set_val(val)

    def get_val(self):
        return self.val

    def set_val(self, val):
        self.val = val

    @abc.abstractmethod
    def showdoc(self):
        return


class GetSetInt(GetterSetter):
    def set_val(self, val):
        if not isinstance(val, int):
            val = 0
        super(GetSetInt, self).set_val(val)

    def showdoc(self):
        print ('GetInt object ({0}), only accepts'
               ' integer values'.format(id(self)))


class GetSetList(GetterSetter):
    def __init__(self, val):
        self.list = [val]

    def get_val(self):
        return self.list[-1]

    def ge_vals(self):
        return self.list

    def set_val(self, val):
        self.list.append(val)

    def showdoc(self):
        print ('GetSetList object len ({0}), stores history'
               ' of values set'.format(len(self.list)))


a = GetSetInt(3)
a2 = GetSetInt('hi')

b = GetSetList(4)
b.set_val(88)
b.set_val(78)

print a.get_val()
print a2.get_val()
a.showdoc()

print b.get_val()
print b.ge_vals()
b.showdoc()
