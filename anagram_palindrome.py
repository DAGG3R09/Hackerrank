#https://www.hackerrank.com/challenges/game-of-thrones

#!/bin/python3
from collections import Counter

import sys

def gameOfThrones(s):
    a = dict(Counter(s))
    flag = 0
    for x in a.values():
        if x%2 != 0:
            flag += 1

    if(flag > 1):
        return "NO"
    else:
        return "YES"

s = input().strip()
result = gameOfThrones(s)
print(result)
