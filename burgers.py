#https://www.hackerrank.com/challenges/jim-and-the-orders?h_r=next-challenge&h_v=zen

import operator

n = int(input())
A = [(i, int(x[0])+int(x[1])) for i,x in
        enumerate([input().split() for i in range(n)], start=1)]

A.sort(key=operator.itemgetter(1,0))
list(map(lambda a: print(a[0], end=" ") ,A))
