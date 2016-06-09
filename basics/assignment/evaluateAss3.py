#!/usr/bin/python
__author__ = 'Mayank'

from assignment3 import MyDict, MyCustomDict

mydict = MyDict('config.txt')
mydict['mayank'] = 'gupta'
mydict['karan'] = 'kapoor'
mydict['mayank'] = 'aggarwal'
mydict['rohit'] = 'sharma'
mydict['karan'] = 'verma'
mydict['john'] = 'doe'

print '\nConfiguration file 1 ::'
print mydict['mayank']
print mydict['karan']
print mydict['rohit']
print mydict['john']

print mydict['Invalid']

myCustomDict = MyCustomDict('config2.txt')
myCustomDict['tom'] = 'jerry'
myCustomDict['mickey'] = 'mini'
myCustomDict['tom'] = 'harry'
myCustomDict['jack'] = 'rose'
myCustomDict['mickey'] = 'mouse'
myCustomDict['bruce'] = 'deck'

print '\n\nConfiguration file 2 ::'
print myCustomDict['tom']
print myCustomDict['mickey']
print myCustomDict['jack']
print myCustomDict['bruce']
