#https://www.hackerrank.com/challenges/gem-stones?h_r=next-challenge&h_v=zen


#!/bin/python3

import sys

def gemstones(arr):
    # Complete this function
    return len(set.intersection(*arr))

n = int(input().strip())
arr = list()
arr_i = 0
for arr_i in range(n):
    arr_t = set(input().strip())
    arr.append(arr_t)

result = gemstones(arr)
print(result)
