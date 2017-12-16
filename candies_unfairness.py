
n = int(input())
k = int(input().strip())
candies = [int(input()) for i in range(n)]
candies.sort()

sum_array = [candies[0]]
[sum_array.append(sum_array[i-1] + candies[i]) for i in range(1,n)]

print(candies,"\n",sum_array)

multiplier = 1-k
answer = 0
for i in range(k):
    answer += multiplier * candies[i]
    multiplier += 2

for i in range(k,n):
    # new_answer = old + items_added + items_removed
    # items removed are negative, thats why add them
    items_added =  (k-1) * candies[i] - (sum_array[i-1] - sum_array[i-k])
    items_removed = (k-1) * candies[i-k] - (sum_array[i-1] - sum_array[i-k])
    new_answer = answer + items_added + items_removed

    final_answer = min (answer, new_answer)
    answer = new_answer

print (final_answer)
