#https://www.hackerrank.com/challenges/lilys-homework/problem


n = int(input())
A = list(map(int, input().split()))


def get_Swaps(A, n):
    hash = {}

    for i in range(n):
        hash[A[i]] = i

    B = sorted(A)
    swaps = 0
    for i in range(n):
        if hash[B[i]] != i:
            swaps += 1

            new_idx = hash[B[i]]
            hash[A[i]] = new_idx
            A[i], A[new_idx] = A[new_idx], A[i]


        #print(hash)
    return(swaps)

s1 = get_Swaps(A, n)
s2 = get_Swaps(list(reversed(A)), n)

print(min(s1, s2))
