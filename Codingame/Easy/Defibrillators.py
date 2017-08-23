import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

lon = raw_input().replace(",", ".")
lat = raw_input().replace(",", ".")
n = int(raw_input())

name = ""
d0 = 100000000.0

for i in xrange(n):
    defib = raw_input().replace(",", ".").split(";")
    x = (float(defib[4]) - float(lon)) * math.cos((float(lat) + float(defib[5])) / 2)
    y = float(defib[5]) - float(lat)
    d = math.sqrt(x*x + y*y) * 6371
    
    if d < d0:
        name = defib[1]
        d0 = d
    
print name
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
