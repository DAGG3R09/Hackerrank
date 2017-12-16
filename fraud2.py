n, d = map(int, raw_input().split())
data = map(int, raw_input().split())
from bisect import bisect


res = 0
vals = sorted(data[:d])
for i in xrange(n-d):
    if d % 2:
        median2 = 2*vals[d/2]
    else:
        median2 = vals[d/2] + vals[d/2-1]
    cur_val = data[d+i]
    if cur_val >= median2:
        res += 1
    #vals change
    to_d = data[i]
    to_a = cur_val
    x = bisect(vals, to_d)
    vals.pop(x-1)
    x = bisect(vals, to_a)
    vals.insert(x, to_a)
    #print vals
print res
