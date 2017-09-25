'''
Casablanca’s hippodrome is organizing a new type of horse racing: duals. During a dual, only two horses will participate in the race.
In order for the race to be interesting, it is necessary to try to select two horses with similar strength.

Write a program which, using a given number of strengths, identifies the two closest strengths and shows their difference with an 
integer (≥ 0).
'''

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(raw_input())
a = sorted([int(raw_input()) for i in range(n)])
d = 100000000

for i in range(n-1):
    d = min(d, a[i+1]-a[i])
    
print d

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
