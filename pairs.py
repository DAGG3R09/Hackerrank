n, k = map(int,input().split())
A = list(map(int,input().split()))
B = set(A)
cnt = 0

for i in A:
    if i-k in B:
        cnt += 1

print(cnt)
