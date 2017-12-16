#https://www.hackerrank.com/challenges/the-love-letter-mystery?h_r=next-challenge&h_v=zen

#!/bin/python3

import sys

def theLoveLetterMystery(s):
    # Complete this function
    i=0
    j=len(s)-1
    cnt = 0
    while i<=j:
        if s[i] != s[j]:
            cnt += abs(ord(s[i]) -ord(s[j]))
        i += 1
        j -= 1

    return cnt

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = theLoveLetterMystery(s)
    print(result)
