from math import ceil, floor

A = [5,4,2,6,1,3]
k = 3
n = len(A)

def swap(arr, n, m):
    t = arr[m]
    arr[m] = arr[n]
    arr[n] = t

def heapify(A, i, n):
    len_A = n
    l = 2*i
    r = 2*i + 1
    smallest = i

    if l < len_A and A[l] < A[smallest]:
        smallest = l
    if r < len_A and A[r] < A[smallest]:
        smallest = r

    if smallest != i:
        swap(A, i, smallest)
        heapify(A, smallest, n)


i = floor(len(A)/2)-1
while i >= 0:
    heapify(A, i, n)
    i -= 1
print(A)

n -= 1
for i in range(k):
    swap(A, 0, n-i)
    heapify(A, 0, n-i)
    print (A)
