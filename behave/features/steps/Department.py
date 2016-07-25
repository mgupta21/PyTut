#!/usr/bin/python
__author__ = 'Mayank'


class Department(object):
    def __init__(self, name, members=None):
        if not members:
            members = []  # Array initialization
        self.name = name
        self.members = members

    def addMember(self, member):
        assert member not in self.members
        self.members.append(member)  # add to array

    @property  # can be used as variable
    def memberCount(self):
        return len(self.members)
