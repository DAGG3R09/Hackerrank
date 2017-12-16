#https://www.hackerrank.com/challenges/sherlock-and-the-beast

#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    Fives = 0
    Threes = 0

    if n % 3 == 0:
        Fives = n // 3
        n = 0
        #print(Fives, " <")

    while n > 0:
        n -= 5
        Threes += 1
        if n % 3 == 0 and n > 0:
            Fives = n // 3
            n = 0
        #print(n)

    #print(">", Fives, Threes)

    s=[]
    if n < 0:
        print(-1)
    else:
        [s.append("555") for i in range (Fives)]
        [s.append("33333") for i in range(Threes)]
        print(''.join(s))
