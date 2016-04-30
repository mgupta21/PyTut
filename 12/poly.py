#!/usr/bin/python
__author__ = 'Mayank'


class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print '{0} is eating {1}.'.format(self.name, food)


class Dog(Animal):
    def fetch(self, obj):
        print '{0} is fetching {1}.'.format(self.name, obj)

    def shows_affection(self):
        print '{0} wags tail!'.format(self.name)


class Cat(Animal):
    def swatstring(self):
        print '{0} shreds the string!'.format(self.name)

    def shows_affection(self):
        print '{0} purrs!!'.format(self.name)


for animal in (Dog('Puppy'), Cat('Betty'), Dog('Tommy'), Cat('Kitty')):
    animal.shows_affection()
