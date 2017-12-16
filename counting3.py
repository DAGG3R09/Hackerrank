from operator import itemgetter
from math import ceil

A = list()
n = int(input())
for i,_ in enumerate(range (n)):
    x, y = input().split()
    A.append((int(x),i,y))

A.sort(key = itemgetter(0,1))

for a in A:
    if a[1] < n/2:
        print("-", end = " ")
    else:
        print(a[2], end = " ")
