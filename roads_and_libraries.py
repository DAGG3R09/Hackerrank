import sys

# def DFS(graph,l,r,visited,start,path=[]):
#     if visited[start] == 1:
#         return
#     visited[start] = 1
#     path.append(start)
#
#     for j in range(len(visited)):
#         if graph[start][j] == 1 and visited[j]!=1:
#             DFS(graph,l,r,visited,j,path)
#     return path

def DFS(graph,l,r,visited,start):
    path = []
    while True:
        flag = 0
        path.append(start)
        visited[start] = 1
        for j in range(len(visited)):
            if graph[start][j] == 1 and visited[j] == 0:
                visited[j] = 1
                start = j
                flag = 1
                break
        if flag == 0:
            return path

q = int(input().strip())
for a0 in range(q):
    n, m, l, r = map (int,input().strip().split(' '))
    graph = [[0 for i in range(n)] for j in range(n)]
    visited = [0 for i in range(n)]
    s = 0

    for a1 in range(m):
        city_1, city_2 = map(int,input().strip().split(' '))
        graph[city_1-1][city_2-1] = 1
        graph[city_2-1][city_1-1] = 1

    if l<r :
        print (l*n)
    else:
        while 0 in visited:
            i = visited.index(0)
            path = DFS(graph,l,r,visited,i)
            print(path)
            s = s + ((len(path)-1)*r) + l
        print(s)
