#!/usr/bin/python
__author__ = 'Mayank'


class NamedNumber(object);
    MAP = {
        "one": 1,
        "two": 2,
        "three": 3,
    }

    @classmethod
    def number_from_string(cls, named_number):
        return cls.MAP.get(named_number)