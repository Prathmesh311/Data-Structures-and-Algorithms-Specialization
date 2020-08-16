# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    currRefill = 0
    numRefills =0

    while stops[numRefills] < d:
        lastRefill = numRefills

        while stops[numRefills]<d and numRefills+1 < len(stops)-1 and stops[numRefills+1] - stops[lastRefill] <=m:
            numRefills = numRefills + 1

        if numRefills == lastRefill:
            return -1
        if stops[numRefills] < d:
            currRefill = currRefill + 1

    return currRefill



if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
