'''
Here is the encoding principle:
    The input message consists of ASCII characters (7-bit)
    The encoded output message consists of blocks of 0
    A block is separated from another block by a space
    Two consecutive blocks are used to produce a series of same value bits (only 1 or 0 values):
        - First block: it is always 0 or 00. If it is 0, then the series contains 1, if not, it contains 0
        - Second block: the number of 0 in this block is the number of bits in the series    
'''

import sys
import math

def bits(c):
    b = []
    for i in range(7):
        b.append(c%2)
        c //= 2
    return b[::-1]

m = raw_input()
bit = []

for c in m:
    bit.extend(bits(ord(c)))
    
first = True
c = 2
ans = ""

for i in bit:
    if i == c:
        ans += "0"
    else:
        if not first:
            ans += " "
        if i == 1:
            c = 1
            ans += "0 0"
        else:
            c = 0
            ans += "00 0"
    first = False

print ans
