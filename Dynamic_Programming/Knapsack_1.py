
def knapsack(wt, val, n, max_wt):
    S = [[0 for _ in range(max_wt+1)] for _ in range(n+1)]

    # print(wt, val)

    for i in range(n+1):
        for w in range(max_wt+1):
            if w == 0 or i == 0:
                S[i][w] = 0
            elif wt[i-1] <= w:
                #either select or dont select
                selected = val[i-1] + S[i-1][w-wt[i-1]]
                not_selected = S[i-1][w]
                S[i][w] = max(selected, not_selected)
            else:
                S[i][w] = S[i-1][w]

    for  j in S:
        print (j)

    i, j = n, max_wt
    weights = []
    while j != 0:
        if S[i-1][j] != S[i][j]:
            weights.append(wt[i-1])
            j -= wt[i-1]
        i -= 1

    return S[n][max_wt], weights

wt = [1, 3, 4, 5]
val = [1, 4, 5, 7]
n = 4
max_wt = 7

print(knapsack(wt,val, n, max_wt))
