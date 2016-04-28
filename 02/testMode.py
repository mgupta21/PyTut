#!/usr/bin/python
__author__ = 'Mayank'

import mode
import modeB as mm  # using alias
from modeC import temp, dothen
from decimal import Decimal

print mode.var
mode.dothis()

print mm.var
mm.dothat()

print temp
dothen()

print Decimal(3.5) + Decimal(6.5)
