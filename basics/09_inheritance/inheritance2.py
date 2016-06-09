#!/usr/bin/python
__author__ = 'Mayank'


class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print '%s is eating %s.' % (self.name, food)


class Dog(Animal):
    def fetch(self, obj):
        print '%s is fetching %s.' % (self.name, obj)


class Cat(Animal):
    def swatstring(self):
        print '%s shreds the string!' % self.name


dog = Dog('Goofy')
dog.fetch('ball')
dog.eat('dog food')

cat = Cat('Kitty')
cat.eat('cat food')
cat.swatstring()
