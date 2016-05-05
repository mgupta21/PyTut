#!/usr/bin/python
__author__ = 'Mayank'

import json

filename = 'config.json'

# laod to/from file

with open(filename) as f:
    json_obj = json.load(f)

print json_obj
print type(json_obj)

json_obj['new_key'] = 'new_val'

with open(filename, 'w') as f:
    json.dump(json_obj, f)

print '\n'

# load to a variable
x = json.dumps({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
y = json.loads(x)

for key in y:
    print key
    for val in y[key]:
        print('     {0}'.format(val))
