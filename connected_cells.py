
def get_connected_cells(mat, i, j, visited):
    visited[i][j] = 1
    for d in directions:
        if (mat[i+d[0]][j+d[1]] == 1
        and visited[i+d[0]][j+d[1]] == 0):
            get_connected_cells(mat, i+d[0], j+d[1], visited)
            continue

    return sum([x.count(1) for x in visited])


n = int(input())
m = int(input())

mat = [[0]*(m+2)]
directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

for i in range(n):
    mx = [0] + list(map(int,input().split())) + [0]
    mat.append(mx)

mat.append([0 for i in range(m+2)])
print (mat)

visited = [[0 for j in range(m+2)] for i in range(n+2)]

connected = 0
cnt = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if mat[i][j] == 1 and visited[i][j] != 1:
            ans = (get_connected_cells(mat, i, j, visited) - cnt)
            cnt += ans

            connected = max(connected, ans)

print(connected)
