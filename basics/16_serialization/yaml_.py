#!/usr/bin/python
__author__ = 'Mayank'

import yaml
import json

this_dict = {'a': 1, 'b': 2, 'c': 3}
this_list = [1, 2, 3, 4, 5]
this_tuple = ('x', 'y', 'z')

yaml_dict = yaml.dump(this_dict, default_flow_style=False)
print yaml_dict

print yaml.dump(this_list, default_flow_style=False)
print yaml.dump(this_tuple, default_flow_style=False)

print '\n\n'

# loading complex obj

obj = (
    [1, 2, 3, 4, 5],
    {'a': 1, 'b': 2, 'c': 3},
    [
        {'x': 98, 'y': 99, 'z': 100},
        11,
        13
    ],
    {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
)

print yaml.dump(obj, default_flow_style=False)

print '\n\n'

# loading form yaml file

with open('deploy.yaml') as f:
    y_obj = yaml.load(f)
    # print y_obj
    print json.dumps(y_obj, indent=4, separators=(',', ': '))
