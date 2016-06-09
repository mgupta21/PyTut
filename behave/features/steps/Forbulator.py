#!/usr/bin/python
__author__ = 'Mayank'


class Forbulator(object):
    def __init__(self, text=None):  # If user calls constructor with no arguments, then pass none to constructor
        self.text = text
        self.activated = False

    def activate(self):
        self.activated = True

    def evaluate_language(self):
        assert self.activated
        assert self.text is not None
        if self.text.startswith("Lorem ipsum"):
            return "English"
        else:
            return "UNKNOWN"
