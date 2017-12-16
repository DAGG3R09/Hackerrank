#https://www.hackerrank.com/challenges/repeated-string

#!/bin/python3

import sys

s = input().strip()
n = int(input().strip())

a = s.count('a')
c = (n // len(s))
x =  s[:(n % len(s))].count('a')

print (a*c + x)
