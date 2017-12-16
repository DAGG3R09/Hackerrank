#https://www.hackerrank.com/challenges/alternating-characters?h_r=next-challenge&h_v=zen

#!/bin/python3

import sys

def alternatingCharacters(s):
    # Complete this function
    i=1
    c = 0
    while i < len(s):
        if s[i] == s[i-1]:
            s.pop(i)
            c += 1
        else:
            i += 1
    return c


q = int(input().strip())
for a0 in range(q):
    s = list(input().strip())
    result = alternatingCharacters(s)
    print(result)
