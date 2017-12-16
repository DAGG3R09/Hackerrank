#https://www.hackerrank.com/challenges/queens-attack-2


def possible_moves(board, direction, current_position, n):

    r = current_position[0] + direction[0]
    c = current_position[1] + direction[1]
    cnt = 0

    while((r,c) not in board
          and r > 0 and r <= n
          and c > 0 and c <= n
         ):

        cnt += 1
        r += direction[0]
        c += direction[1]
    return cnt

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]

board = set()

rQueen,cQueen = input().strip().split(' ')
rQueen,cQueen = [int(rQueen),int(cQueen)]

for a0 in range(k):
    rObstacle, cObstacle = input().strip().split(' ')
    rObstacle, cObstacle = [int(rObstacle),int(cObstacle)]
    # your code goes here
    board.add((rObstacle, cObstacle))

positions = 0
moves = [(0,-1), (0,1), (1,0), (-1,0), (1,-1), (-1, 1), (-1,-1), (1,1)]

for move in moves:
    positions += possible_moves(board, move, (rQueen, cQueen), n)

print(positions)
