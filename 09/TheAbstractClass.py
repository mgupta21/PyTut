#!/usr/bin/python
__author__ = 'Mayank'

# Python abc module enables creation of abstract base classes
import abc


class GetterSetter(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_val(self):
        """Get and return a value from instance"""
        return

    @abc.abstractmethod
    def set_val(self):
        """Set a value in the instance"""
        return


class MyClas(GetterSetter):
    def get_val(self):
        return self.val

    def set_val(self, val):
        self.val = val


a = MyClas()
a.set_val(33)
print a.get_val()
