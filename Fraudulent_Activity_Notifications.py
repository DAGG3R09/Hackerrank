#https://www.hackerrank.com/challenges/fraudulent-activity-notifications

import sys

def kth_smallest_term(frequency, k):
    i = 0
    for i in range(len(frequency)):
        k -= frequency[i]
        if k <0 :
            return i
    return -1

def activityNotifications(A, d):
    frequency = [0 for i in range(200)]

    # print(frequency)
    print("----------------------")
    input()
    print(A[2000])
    for i in range(d):
        # print(i, end= " ")
        index = A[i]
        frequency[index] += 1

    notifi = 0
    # print(frequency)

    for i in range(d, n):
        print(A[i-d-i:i])
        med = kth_smallest_term(frequency, d // 2)
        if d % 2 == 0:
            med = (kth_smallest_term(frequency, (d//2) - 1) + med) /2

        # print(med)
        if (2*med) <= A[i]:
            notifi += 1

        frequency[A[i-d-1]] -= 1
        frequency[A[i]] += 1

    return notifi

if __name__ == "__main__":
    n, d = input().strip().split(' ')
    n, d = [int(n), int(d)]
    expenditure = (map(int, input().strip().split(' ')))
    result = activityNotifications(expenditure, d)
    print(result)
