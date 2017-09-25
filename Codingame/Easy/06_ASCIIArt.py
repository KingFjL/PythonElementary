'''
    Your mission is to write a program that can display a line of text in ASCII art in a style you are given as input.
'''


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

L = int(raw_input())
H = int(raw_input())
T = list(raw_input())

for i in range(len(T)):
    #isalpha() 方法检测字符串是否只由字母组成
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
        """
        ord()函数是chr()函数（对于8位的ASCII字符串）或unichr()函数（对于Unicode对象）的配对函数，
        它以一个字符（长度为1的字符串）作为参数，返回对应的ASCII数值，或者Unicode数值，如果所给的
        Unicode字符超出了你的Python定义范围，则会引发一个TypeError的异常。
        """
        ans += set[i][n:n+L]
    ans += "\n"
print ans

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
