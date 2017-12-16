s = input().strip()
n = int(input())

a = ord('a')-1

solutions = [ord(s[0])-a]
for i in range(1,len(s)):
    if s[i] == s[i-1]:
        solutions.append(solutions[i-1]+(ord(s[i])-a))
    else:
        solutions.append(ord(s[i])-a)

solutions = set(solutions)
# print(solutions)

for a0 in range(n):
    x = int(input().strip())
    if x in solutions:
        print("Yes")
    else:
        print("No")
