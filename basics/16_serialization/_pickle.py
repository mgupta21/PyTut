#!/usr/bin/python
__author__ = 'Mayank'

import pickle

filename = 'datafile.txt'
filenameB = 'datafileB.txt'

# storing to a file

my_list = ['a', 'b', 'c', 'd', 'e']

with open(filename, 'w') as f:
    pickle.dump(my_list, f)

with open(filename) as f:
    un_pickled_list = pickle.load(f)

print un_pickled_list
print '\n\n'

# storing to object

x = pickle.dumps(['1', 3.4, 'N', 4])  # dumpS
y = pickle.loads(x)  # loadS
print y
print '\n\n'

# loading complex objects

this_int = 534
this_string = 'this is a string'
this_dict = {
    'a': [1, 2, 3],
    'b': [4, 5, 6]
}
this_query_list = [('john', 67, 'tester'), ('brian', 32, 'developer'), ('adam', 53, 'product owner')]

with open(filenameB, 'w') as f:
    pickle.dump((this_int, this_string, this_dict, this_query_list), f)

with open(filenameB) as f:
    tup = pickle.load(f)

for t in tup:
    print t
