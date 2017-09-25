'''
The input data you require for your program is provided in text format.
This data is comprised of lines, each of which represents a defibrillator. Each defibrillator is represented by the following fields:
    · A number identifying the defibrillator
    · Name
    · Address
    · Contact Phone number
    · Longitude (degrees)
    · Latitude (degrees)
These fields are separated by a semicolon (;).

Beware: the decimal numbers use the comma (,) as decimal separator. Remember to turn the comma (,) into dot (.) if necessary in order 
to use the data in your program.
 
DISTANCE
The distance d between two points A and B will be calculated using the following formula:
    · x = (longitudeB - longitudeA) * cos((latitudeA + latitudeB)/2)
    · y = (latitudeB - latitudeA)
    · d = √(x^2+y^2) * 6371
    
Note: In this formula, the latitudes and longitudes are expressed in radians. 6371 corresponds to the radius of the earth in km.

The program will display the name of the defibrillator located the closest to the user’s position. This position is given as input
to the program.
'''

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
