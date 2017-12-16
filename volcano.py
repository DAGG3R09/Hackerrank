#!/bin/python3

import sys

def erupt_volcano(mat, x, y, w, n):
    mat[x][y] += w
    w -= 1
    tx = x
    ty = y

    #up
    for i in range(w,0,-1):
        x -= 1
        if x<0: break
        mat[x][y] += i
    x = tx

    #down
    for i in range(w,0,-1):
        x += 1
        if x>=n: break
        mat[x][y] += i
    x = tx

    #left
    for i in range(w,0,-1):
        y-=1
        if y<0: break
        mat[x][y] += i
    y = ty

    #right
    for i in range(w,0,-1):
        y += 1
        if y>=n: break
        mat[x][y] += i
    y = ty

    #upleft
    for i in range(w,0,-1):
        x -= 1
        y -= 1
        if x<0 or y<0: break
        mat[x][y] += i
    x = tx
    y = ty

    #upright
    for i in range(w,0,-1):
        x -= 1
        y += 1
        if x<0 or y>=n: break
        mat[x][y] += i
    x = tx
    y = ty


    #botleft
    for i in range(w,0,-1):
        x += 1
        y -= 1
        if x>=n or y<0: break
        mat[x][y] += i
    x = tx
    y = ty

    #botright
    for i in range(w,0,-1):
        x += 1
        y += 1
        if x>=n or y>=n: break
        mat[x][y] += i


    for x in mat:
        print(x)


if __name__ == "__main__":
    n = int(input().strip())
    m = int(input().strip())
    mat = [[0 for i in range(n)] for j in range(n)]

    for a0 in range(m):
        x, y, w = input().strip().split(' ')
        x, y, w = [int(x), int(y), int(w)]
        # Write Your Code Here
        erupt_volcano(mat, x, y, w, n)

    maxi = 0
    for x in mat:
        maxi = max(max(x), maxi)

    print(maxi)
