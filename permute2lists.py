
q = int(input())

for _ in range (q):
    n, k = map (int,input().split(" "))
    A = list(map (int,input().split(" ")))
    B = list(map (int,input().split(" ")))
    i = 0
    j = n-1
    A.sort()
    B.sort()

    while i<n:
        if A[i]+B[j]>=k:
            i+=1
            j-=1
        else:
            print("NO")
            break

    if i==n:
        print("YES")
