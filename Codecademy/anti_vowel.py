"""
For example: 
anti_vowel("Hey You!") should return "Hy Y!". 
Don't count Y as a vowel. Make sure to remove lowercase and uppercase vowels.
"""

def anti_vowel(text):
    t=""
    for c in text:
        for i in "ieaouIEAOU":
            if c==i:
                c=""
            else:
                c=c
        t=t+c
    return t
