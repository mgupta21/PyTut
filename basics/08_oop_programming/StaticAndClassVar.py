#!/usr/bin/python
__author__ = 'Mayank'


# class method takes class as argument and works on class object

class InstanceCounter(object):
    count = 0

    def __init__(self, val):
        self.value = self.filter_int(val)
        self.increment_count()

    @staticmethod
    def filter_int(val):
        if isinstance(val, int):
            return val
        else:
            return 0

    @classmethod
    def get_count(cls):
        return cls.count

    def get_value(self):
        return self.value

    @classmethod
    def increment_count(cls):
        cls.count += 1


a = InstanceCounter(42)
b = InstanceCounter(32)
c = InstanceCounter('hi')

print a.get_value()
print a.get_count()

print b.get_value()
print b.get_count()

print c.get_value()
print c.get_count()
