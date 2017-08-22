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
