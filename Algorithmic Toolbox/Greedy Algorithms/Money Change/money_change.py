# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    if money==2:
        return 2

    coins10 = int(money/10)
    rem10   = int(money%10)
    coins5  = int(rem10/5)
    rem5    = int(rem10%5)
    coins1  = int(rem5/1)

    totalCoins = coins10 + coins5 + coins1
    return totalCoins


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
