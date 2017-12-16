
def kth_smallest_term(frequency, k):
    i = 0
    for i in range(len(frequency)):
        k -= frequency[i]
        if k <0 :
            return i
    return -1

def start(A, n, d):
    frequency = [0 for i in range(max(A)+1)]
    for i in range(d):
        frequency[A[i]] += 1


    for i in range(d+1, n):
        med = kth_smallest_term(frequency, d // 2)
        if d % 2 == 0:
            med = (kth_smallest_term(frequency, (d//2) - 1) + med) /2

        frequency[A[i-1]] -= 1
        frequency[A[i]]+= 1




A = [17, 3, 12, 6, 8, 2, 7]
start(A, len(A), 3)
A.sort()
print(A, A[len(A)//2])
