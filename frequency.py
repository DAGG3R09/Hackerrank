from collections import Counter

import sys

def isValid(strng):
    c = Counter(strng)
    values = list(c.values())
    f = Counter(values)
    frequency = f.most_common(1)[0][0]
    print(c,frequency)
    cnt = 0
    for value in values:
        if value == 1:
            cnt +=1
            continue
        cnt+= abs(value-frequency)

    if (cnt <= 1 ):
        return "YES"
    return "NO"

s = input().strip()
result = isValid(s)
print(result)
