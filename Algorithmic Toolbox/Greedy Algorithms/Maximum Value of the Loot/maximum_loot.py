# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    Sorted = [prices[i]/weights[i] for i in range(len(prices))]
    #newWeights = []
    #newPrices = []
    '''for i in range(len(prices)):
        maxNum = max(Sorted)
        newWeights[i] = weights[(weights.index(maxNum))]
        newPrices[i]  = prices[prices.index(maxNum)]
        prices.remove(maxNum)
    '''
    value=0
    for i in range(len(prices)):
        if capacity==0:
            return value

        index = 0
        for s in range(len(prices)+1):
            if weights[s]>0:
                return value
            maxNum = max(Sorted)
            index = Sorted.index(maxNum)
            Sorted.remove(maxNum)

        a = min(weights[index], capacity)
        value = value + a*(prices[index]/weights[index])

        weights[index] = weights[index] - a
        capacity = capacity - a



    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
