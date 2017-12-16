q = int(input())

for a0 in range(q):
    n = input()

    if n.startswith("0"):
        print("NO")
        continue

    flag = 0
    for i in range(1, len(n)):
        x = str(int(n[0:i]) + 1)
        if n[i :].startswith(x):
            flag = 1
        else:
            continue

        y = int(x)-1

        temp = i
        i = i+len(x)
        while i < len(n):
            x = str(int(x)+1)
            if n[i:].startswith(x):
                i = i+len(x)
            else:
                flag = 0
                i = temp
                break

        if i >= len(n):
            print("YES",y)
            break

    if flag == 0 :
        print("NO")
        continue
