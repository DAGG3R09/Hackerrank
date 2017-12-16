##https://www.hackerrank.com/challenges/even-tree/problem

vertices, edges = list(map(int, input().split()))

tree = dict()
visited = [None for i in range(vertices)]
weight = [1 for i in range(vertices)]

def DFS(visited, tree, vertex):
    visited[vertex-1] = True

    children = tree[vertex]

    for child in children:
        if visited[child-1] == None:
            weight[vertex -1] += DFS(visited, tree, child)

    return weight[vertex -1]


for i in range(edges):
    d, s = list(map(int, input().split()))
    if s not in tree.keys():
        tree[s] = [d]
    else:
        tree[s].append(d)

    if d not in tree.keys():
        tree[d] = []


DFS(visited, tree, 1)
print(len(list(filter(lambda a: a%2 == 0, weight)))-1)
