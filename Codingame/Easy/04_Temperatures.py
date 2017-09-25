'''
    In this exercise, you have to analyze records of temperature to find the closest to zero
'''

import sys
import math


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(raw_input())
temps = raw_input()

a = sorted([int(i) for i in temps.split()], reverse=True)

if len(a)==0:
    print "0"
else:
    print min(a, key=lambda x:abs(x))
            
          
# To debug: print >> sys.stderr, "Debug messages..."
 
