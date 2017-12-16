
def get_white_ball(balls,i):
    if balls[i] == 'W' or balls[len(balls)-i-1] == 'W':
        return True
    return False

def get_probabilty(balls_orientations):
    p=0
    for balls in balls_orientations:
        x = 0
        for i in range(len(balls)):
            if get_white_ball(balls,i):
                x+=1
        p += x/len(balls) * 1/len(balls_orientations)

    return p

def remove_white_ball(orientations):
    all_orientations = set()
    for balls in orientations:
        for i in range(len(balls)):
            if balls[i] == "W":
                all_orientations.add(balls[:i]+balls[i+1:])
    return (all_orientations)

def choose_white_balls(balls,k):
    if k == 0:
        return 0

    p = get_probabilty(balls)
    balls = remove_white_ball(balls)
    return p + choose_white_balls(balls,k-1)

# n, k = map (int,input().split(" "))
# balls = [input()]
# print(choose_white_balls(balls,k))
# print(choose_white_balls(["BWBBBW"],4))

# print(remove_white_ball(["BWWBWW"]))

print(get_probabilty(["BWBBBW"]))
print(remove_white_ball(["BWBBBW"]))
print(get_probabilty(remove_white_ball(["BWBBBW"])))
