#!/bin/python3

import sys

def solve(A):
    left = 0
    right= sum(A[1:])
    for i in range(len(A)-1):
        if left == right:
            return "YES"
        left+= A[i]
        right-=A[i+1]

    # print(left,right)
    if left == right:
        return "YES"
    return("NO")

T = int(input().strip())
for a0 in range(T):
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = solve(a)
    print(result)
