import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

L = int(raw_input())
H = int(raw_input())
T = list(raw_input())

for i in range(len(T)):
    if T[i].isalpha():
        T[i] = T[i].upper()
    else:
        T[i] = '['
        
#T = ''.join(T)#可有可无
set = [ raw_input() for i in range(H)]
ans = ""

for i in range(H):
    for c in T:
        n = (ord(c) - ord('A'))*L
        ans += set[i][n:n+L]
    ans += "\n"
print ans

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
