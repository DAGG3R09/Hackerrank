#https://www.hackerrank.com/challenges/recursive-digit-sum/

n, k = list(map(int, input().split()))


n = sum(map(int, list(str(n)))) * k
l = len(str(n))
while (l != 1):
    n = sum(map(int, list(str(n))))
    l = len(str(n))

print(n)
