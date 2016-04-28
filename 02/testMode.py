#!/usr/bin/python
__author__ = 'Mayank'

import mode
import modeB as mm  # using alias
from modeC import temp, dothen
from decimal import Decimal

print mode.var
print mode.dothis()

print mm.var
print mm.dothat()

print temp
print dothen()

print Decimal(3.5) + Decimal(6.5)
