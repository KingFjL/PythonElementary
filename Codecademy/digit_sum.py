"""
For example: 
digit_sum(1234) should return 10 which is 1 + 2 + 3 + 4. 
(Assume that the number you are given will always be positive.)
"""

def digit_sum(x):
    total = 0
    while x > 0:
        total += x % 10
        x = x // 10
        print x
    return total
