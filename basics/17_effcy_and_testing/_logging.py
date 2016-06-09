#!/usr/bin/python
__author__ = 'Mayank'

import logging

logging.basicConfig(format='%(asctime)s   %(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

logging.debug('This is a debugged message')
logging.info('This is a informational message')
logging.warning('This is a warning message')
logging.error('This is an error message')