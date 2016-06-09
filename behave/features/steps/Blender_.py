#!/usr/bin/python
__author__ = 'Mayank'


class Blender(object):
    TRANSFORMATION_MAP = {
        "iPhone": "toxic waste",
        "nexus": "toxic waste",
        "oranges": "orange juice",
        "apples": "apple juice",
        "red tree frog": "mush"
    }

    def __init__(self):
        self.thing = None
        self.other_thing = None

    @classmethod
    def select_result_for(cls, thing):
        return cls.TRANSFORMATION_MAP.get(thing)

    def insert(self, thing):
        self.thing = thing

    def switch_on(self):
        self.other_thing = self.select_result_for(self.thing)
