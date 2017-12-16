#https://www.hackerrank.com/challenges/funny-string

#!/bin/python3

import sys

def funnyString(s):
    # Complete this function
    i = 1
    j = len(s)-1
    while(j>=0):
        if abs(ord(s[i-1])- ord(s[i])) != abs(ord(s[j-1])-ord(s[j])):
            return "Not Funny"

    return "Funny"

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = funnyString(s)
    print(result)
