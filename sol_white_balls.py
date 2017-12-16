#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
balls = input().strip()
# your code goes here
cnt = balls.count('W')
memo = {}

def dfs(depth, S):
    if S in memo: return memo[S]
    if depth == k: return cnt - S.count('W')
    res = 0
    length = n - depth
    for i in range(length // 2):
        print(S[:i] + S[i + 1:])
        left = dfs(depth + 1, S[:i] + S[i + 1:])
        right = dfs(depth + 1, S[:length - 1 - i] + S[length - i:])
        res += max(left, right)
    res *= 2
    if length % 2 == 1: res += dfs(depth + 1, S[:length // 2] + S[length // 2 + 1:])
    memo[S] = res
    return res

if n == k:
    print(cnt)
else:
    ans = dfs(0, balls)
    for i in range(k): ans /= n - i
    print("%.8f" % ans)
