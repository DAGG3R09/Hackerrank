#https://www.hackerrank.com/contests/pucsd-17-18-test-7/challenges/kaprekar-numbers/copy-from/1303699965

from math import ceil

def is_karpekar_number(n):
    #if n==1:
    #    return True

    x = int(n *n)
    length = len(str(x))
    half = ceil(length / 2)

    multiplier = 10 ** (half)
    l = x // multiplier
    r = x % multiplier
    #print(n, x, l, r, l+r, length, half, multiplier)

    if l+r == n and r != 0:
        return True

    return False

p = int(input())
q = int(input())

flag = 0

#print(is_karpekar_number(1))

for i in range(p,q+1):
    if(is_karpekar_number(i)):
        print(i,end = " ")
        flag = 1

if flag == 0:
    print("INVALID RANGE")
