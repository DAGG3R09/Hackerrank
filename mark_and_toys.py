#https://www.hackerrank.com/challenges/mark-and-toys/problem

#!/bin/python3

import sys

def maximumToys(prices, k):
    # Complete this function
    prices.sort()
    i = 0
    while k > prices[i]:
        k -= prices[i]
        i += 1

    return i
if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    prices = list(map(int, input().strip().split(' ')))
    result = maximumToys(prices, k)
    print(result)
