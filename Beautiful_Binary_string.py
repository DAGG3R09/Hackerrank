#https://www.hackerrank.com/challenges/beautiful-binary-string?h_r=next-challenge&h_v=zen

#!/bin/python3

import sys

def minSteps(n, B):
    # Complete this function
    c = 0
    i = 0
    while i < n-2:
        if B[i] == '0' and B[i+1] == '1' and B[i+2] == '0':
            B[i+2] = 1
            c += 1
            i += 2
        else:
            i +=1
    return c

n = int(input().strip())
B = list(input().strip())
result = minSteps(n, B)
print(result)
