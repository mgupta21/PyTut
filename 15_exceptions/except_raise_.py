#!/usr/bin/python
__author__ = 'Mayank'

import re


def process_date(this_date):
    # this regex ensures date is in YYYY-MM-DD format
    if not re.search(r'^\d\d\d\d\-\d\d\-\d\d$', this_date):
        raise ValueError('please submit date in YYYY-MM-DD format')
    else:
        print('Submitted date is {0}'.format(this_date))


process_date('1999-12-31')
process_date('31/12/1999')
