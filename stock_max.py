#https://www.hackerrank.com/challenges/stockmax/problem

q = int(input())

for a0 in range(q):
    n = int(input())
    A = list(map(int, input().split()))
    current_max = A[n-1]
    profit = 0
    for i in range(n-2, -1, -1):
        if A[i] > current_max:
            current_max = A[i]
        else:
            profit += (current_max - A[i])

    print(profit)
