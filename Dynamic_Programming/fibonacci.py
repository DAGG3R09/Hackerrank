# n = int(input())


def iterative_memoized(n, A):
    for i in range(n):
        if A[i] == -1:
            A[i] = A[n-1] + A[n-2]
    return A[n]

def fibo_memozied(n, A):
    if A[n] != -1:
        return A[n]

    A[n] = fibo_memozied(n-1, A) + fibo_memozied(n-2, A)
    return A[n]

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)

n = 6
A = [-1 for i in range(n+1)]
A[0] = 0
A[1] = 1

print(fibonacci(n))
print(fibo_memozied(n, A))
print(iterative_memoized(n, A))
