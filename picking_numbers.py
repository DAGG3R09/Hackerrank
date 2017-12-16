#https://www.hackerrank.com/challenges/picking-numbers

from collections import Counter
from operator import itemgetter

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]

ans = []

s = dict(Counter(a))
for k,v in s.items():
    ans.append((k,v))

ans.sort(key=itemgetter(0))
sol = 0

for i in range(1,len(ans)):
    if ans[i][0] - ans[i-1][0] == 1:
        m = ans[i][1] + ans[i-1][1]
        if m > sol:
            sol = m


x = max(ans,key=itemgetter(1))
if x[1] > sol:
    sol = x[1]

print (sol)
