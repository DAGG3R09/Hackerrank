n,d = [int (x) for x in input("").split()]
numbers = [int(x) for x in input("").split()]

if n>10**5:
    exit()
elif d<1 or d>n:
    exit()
else:
    while d:
        num = numbers.pop(0)
        numbers.append(num)
        d-=1

    # print (numbers,n,d)
    for n in numbers:
        print (n,end=" ")
