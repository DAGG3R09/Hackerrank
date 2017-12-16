q = int(input())

for a0 in range(q):
    n = int(input())
    A = list(map (int,input().split()))
    sublist_sum = [a for a in A]
    max_sum = A[0]

    for i in range(1,len(A)):
        m = sublist_sum[i-1] + A[i]
        if m > sublist_sum[i]:
            sublist_sum[i] = m
        if max_sum + A[i] > max_sum:
            max_sum+=A[i]
        if max_sum < A[i]:
            max_sum = A[i]

    print(max(sublist_sum),max_sum)
