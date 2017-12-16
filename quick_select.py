
# finding median using quick select algorithm

def swap(A, i, j):
    t = A[i]
    A[i] = A[j]
    A[j] = t

def partition(A, left, right):
    pivot = A[left]
    swap (A, left, right)
    store_index = 0
    print(A[right], A)
    for i in range(right):
        if A[i] <= pivot:
            swap(A, store_index, i)
            store_index += 1
    swap(A, store_index, right)

    return store_index

def kth_smallest_term(A, n, k):
    mid_term = k
    left = 0
    right = n-1

    while True:
        pivot_index = partition(A, left, right)

        if pivot_index == mid_term:
                return A[mid_term]
        elif mid_term < pivot_index:
            right = pivot_index -1
        else:
            left = pivot_index + 1


def median(A, n):
    mid = n // 2
    ans = kth_smallest_term(A, n, mid)
    if n % 2 == 0:
        ans = (kth_smallest_term(A, n, mid-1) + ans) / 2
    return ans


A = [4, 3, 1, 6, 8, 2]
print(median(A, len(A)))
