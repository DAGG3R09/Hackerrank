#https://www.hackerrank.com/challenges/determining-dna-health?h_r=next-challenge&h_v=zen


### incomplete
#!/bin/python3

import sys
import re

n = int(input().strip())
genes = input().strip().split(' ')
health = list(map(int, input().strip().split(' ')))
s = int(input().strip())
min = None
max = None


for a0 in range(s):
    first,last,d = input().strip().split(' ')
    first,last,d = [int(first),int(last),str(d)]
    # your code goes here

    current_health = 0

    for i in range(first, last+1):
        gene = genes[i]
        g_value = health[i]

        x = "(?="+gene+")"
        current_health += len(re.findall(x, d)) * g_value


    if (max < current_health or max == None):
        max = current_health
    if (min > current_health or min == None):
        min = current_health

print(min, max)
