n = int(input())
counts = [0] * 100
helper = [[] for i in range(100)]

for i in range(n):
    arr = input().split()
    num = int(arr[0])
    counts[num] = counts[num] + 1
    helper[num].append((i, arr[1]))

for h in helper:
    print (h)
