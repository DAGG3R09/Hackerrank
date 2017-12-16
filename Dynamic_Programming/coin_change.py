def coin_change(coins, total):
    S = [100000 for _ in range(total+1)]
    S[0] = 0
    L = [-1 for _ in range(total+1)]

    for i in range(len(coins)):
        if coins[i] > total:
            continue
        for j in range(1, total+1):
            if coins[i] <= j:
                new_coins = 1 + S[j-coins[i]]
                if S[j] > new_coins:
                    S[j] = new_coins
                    L[j] = i

        print(coins[i], S)
        print(L)

    coins_used = []
    i = L[n]
    while total != 0:
        coins_used.append(coins[i])
        total -= coins[i]
        i = L[total]

    return S[n], coins_used

# coins = [8, 3, 1, 2]
coins = [7, 2, 3, 6]
n = 12
print(coin_change(coins, n))
