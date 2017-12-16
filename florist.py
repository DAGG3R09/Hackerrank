def getMinimumCost(n, k, c):
    i=1
    s=0
    x = n-k
    y=n

    while y>=0:
        s+=sum(c[x:y])*i
        x-=k
        if x<0: x=0
        y-=k
        i+=1
    return s

n, k = [int (n) for n in input().split(' ')]
c = [int(x) for x in input().split(' ')]
c.sort()


minimumCost = getMinimumCost(n, k, c)
print(minimumCost)
