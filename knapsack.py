#https://www.hackerrank.com/challenges/unbounded-knapsack/problem

def knapsack(numbers, e_sum, i, n):
    if i>=n:
        return 0

    if numbers[i] <= e_sum:
        m1 = knapsack(numbers, e_sum-numbers[i], i, n) + numbers[i]
        m2 = knapsack(numbers, e_sum-numbers[i], i+1, n) + numbers[i]
        m3 = knapsack(numbers, e_sum, i+1, n)
        return max(m1, m2, m3)

    return 0

q = int(input())

for a0 in range(q):
    n, e_sum = map (int, input().split())
    numbers = list(map (int, input().split()))
    numbers = list(set(numbers))
    numbers.sort()

    flag = 0
    for n in numbers:
        if e_sum % n == 0:
            print(e_sum)
            flag = 1
            break

    if flag == 1:
        continue

    print(knapsack(numbers, e_sum, 0, len(numbers)))
