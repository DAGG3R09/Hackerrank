input()
A = [int(a) for a in input().split()]
input()
B = [int(a) for a in input().split()]
ans = []

for a in A:
    if a in B:
        B.remove(a)

B = list(set(B))

B.sort()

for a in B:
    print (a, end=" ")
