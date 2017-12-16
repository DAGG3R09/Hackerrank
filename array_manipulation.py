#!/bin/python3

# import sys
#
# if __name__ == "__main__":
#     n, m = input().strip().split(' ')
#     n, m = [int(n), int(m)]
#     array = [0 for i in range(n)]
#
#     for a0 in range(m):
#         a, b, k = input().strip().split(' ')
#         a, b, k = [int(a), int(b), int(k)]
#         for i in range(a-1,b):
#             array[i]+=k
#
#     print(max(array))


n, inputs = [int(n) for n in input().split(" ")]
list = [0 for i in range(n+1)]

for _ in range(inputs):
    x, y, incr = [int(n) for n in input().split(" ")]
    list[x-1] += incr
    if((y)<=len(list)): list[y] -= incr;
    print(list)

max = x = 0

for i in list:
   x=x+i;
   if(max<x): max=x;
print(max)
