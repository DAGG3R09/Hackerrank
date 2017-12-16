q = int(input())
x = 10 ** 9 + 7

for _ in range (q):
    n, k = map (int,input().split(" "))
    A = list(map (lambda a : (int(a), 0), input().split(" ")))
    B = list(map (lambda a : (int(a), 1), input().split(" ")))
    L = A+B
    L.sort(reverse=True)
    pieces = [1,1] #(Horizontal,Vertical)
    cost = 0

    for cut in L:
        cost += cut[0] * pieces[cut[1]]
        pieces[(cut[1]+1)%2]+=1



    print(cost% x)
