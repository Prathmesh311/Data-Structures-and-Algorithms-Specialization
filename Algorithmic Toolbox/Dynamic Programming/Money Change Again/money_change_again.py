# python3


def change_naive(money):
    min_coins = float("inf")

    for num1 in range(money + 1):
        for num3 in range(money // 3 + 1):
            for num4 in range(money // 4 + 1):
                if 1 * num1 + 3 * num3 + 4 * num4 == money:
                    min_coins = min(min_coins, num1 + num3 + num4)

    return min_coins


def change(money):
    minCoins = []
    minCoins.append(0)

    coins = [1, 3, 4]

    for i in range(1, money + 1):
        minCoins.append(i + 1)
        for j in (1, 3, 4):
            if i >= j:
                # numCoins = min(numCoins,minCoins[i-coins[j]] + 1)
                numCoins = minCoins[i - j] + 1
                if numCoins < minCoins[i]:
                    minCoins[i] = numCoins
        # minCoins[i] = numCoins

    return minCoins[money]


if __name__ == '__main__':
    amount = int(input())
    coins = [1, 3, 4]
    print(change(amount))
    # print(coin_change(coins,amount,2))
