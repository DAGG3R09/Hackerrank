
n = int(input())
k = int(input())
A = [int(input()) for i in range(n)]
A.sort()

x = 0
y = k

unfairness = A[y-1]-A[x]
x+=1
y+=1

while y<=n:
    # print(A[x:y])
    new_unfair = A[y-1]-A[x]
    if unfairness > new_unfair: unfairness = new_unfair
    x+=1
    y+=1

print(unfairness)
