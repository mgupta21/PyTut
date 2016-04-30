#!/usr/bin/python
__author__ = 'Mayank'

import random


class Animal(object):
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.breed = random.choice(['Lebrador', 'German Shepherd', 'Bulldog', 'Golden Retriever'])


for dog in (Dog('Spot'), Dog('Scooby'), Dog('Tom'), Dog('Timothy')):
    print '{0} belongs to {1} breed.'.format(dog.name, dog.breed)
