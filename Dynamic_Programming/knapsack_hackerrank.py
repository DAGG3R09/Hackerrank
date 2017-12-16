#https://www.hackerrank.com/challenges/unbounded-knapsack/problem

def knapsack(numbers, e_sum, n):
    S = [0 for _ in range(e_sum+1)]

    for i in range(n):
        if numbers[i-1] > e_sum:
            continue
        for current_sum in range(1, e_sum+1):
            if numbers[i-1] <= current_sum:
                S[current_sum] = max(S[current_sum], numbers[i-1]+ S[current_sum - numbers[i-1]])
        #print (S)

    return S[e_sum]

q = int(input())

for a0 in range(q):
    # n, e_sum = map (int, input().split())
    # numbers = list(map (int, input().split()))
    # numbers = list(set(numbers))
    # numbers.sort()

    n, e_sum = 3, 12
    numbers = [1, 6, 9]

    print(knapsack(numbers, e_sum, len(numbers)))
