#https://www.hackerrank.com/challenges/closest-numbers

input()

A = list(map(int, input().split()))
S = [0 for i in A]
A.sort()

min = None

for i in range (1, len(A)):
    S[i] = A[i] - A[i-1]
    if min == None or min > S[i] :
        min = S[i]

for i in range (1, len(A)):
    if S[i] == min:
        print(A[i-1], A[i], end=" ")
