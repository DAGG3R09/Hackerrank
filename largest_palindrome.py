#!/bin/python3
#https://www.hackerrank.com/challenges/richie-rich?h_r=next-challenge&h_v=zen

from math import floor

def richieRich(s, n, k):
    # Complete this function
    i = 0
    x = n
    n-=1
    mid = floor(x/2)

    unmatched = 0
    while i<=n:
        if s[i] != s[n]:
            unmatched+=1
        i+=1
        n-=1

    extra_moves = k - unmatched
    # print(unmatched, extra_moves)

    if extra_moves < 0:
        return -1

    n = x-1
    i = 0
    while extra_moves > 0 and i<=n:
        if extra_moves >= 2 and s[i] == s[n] and s[i] != "9":
            s = s[:i]+"9"+s[i+1:]
            s = s[:n]+"9"+s[n+1:]
            extra_moves -= 2

        if s[i] != s[n] and s[i] != "9" and s[n] != "9":
            s = s[:i]+"9"+s[i+1:]
            extra_moves -= 1

        print(extra_moves)

        i += 1
        n -= 1

    if  extra_moves >=1 and x%2==1 and s[mid]!="9":
        s = s[:mid]+"9"+s[mid+1:]
        extra_moves -= 1


    n = x-1
    i = 0
    while k > 0 and i <= n:
        if s[i] != s[n]:
            if s[i] < s[n]:
                s= s[:i]+s[n]+s[i+1:]
            else:
                s= s[:n]+s[i]+s[n+1:]
            k-=1
        i+=1
        n-=1


    # while extra_moves >=2 and i<n :
    #     if s[i] != "9" and s[n] != "9":
    #         if s[i]!!=s[n]:
    #             extra_moves += 1
    #
    #         s= s[:i]+"9"+s[i+1:]
    #         s= s[:n]+"9"+s[n+1:]
    #         extra_moves-=2
    #
    #     i+=1
    #     n-=1
    #
    # n = x-1
    # i = 0
    # while extra_moves == 1:
    #
    #
    # n = x-1
    # i = 0
    #
    # while i<n:
    #     if s[i] != s[n]:
    #         if extra_moves >=1 and s[i] != "9" and s[n] != "9":
    #             s= s[:i]+"9"+s[i+1:]
    #             s= s[:n]+"9"+s[n+1:]
    #         elif s[i] < s[n]:
    #             s= s[:i]+s[n]+s[i+1:]
    #         else:
    #             s= s[:n]+s[i]+s[n+1:]
    #         k-=1
    #     i+=1
    #     n-=1

    return s

n, k = map(int,input().split())
s = input().strip()
result = richieRich(s, n, k)
print(result)
