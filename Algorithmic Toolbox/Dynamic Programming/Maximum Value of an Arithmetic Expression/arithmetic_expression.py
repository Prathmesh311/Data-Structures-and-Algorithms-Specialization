# python3
import math
def evaluate(part1, part2, operation):
    if operation == "+":
        return part1 + part2
    elif operation == "-":
        return part1 - part2
    elif operation == "*":
        return part1 * part2
    else:
        assert False


def min_and_max(M, m, i, j, operations):
    minimum = math.inf
    maximum = -math.inf

    for k in range(i, j):
        a = evaluate(M[i][k], M[k + 1][j], operations[k])
        b = evaluate(M[i][k], m[k + 1][j], operations[k])
        c = evaluate(m[i][k], M[k + 1][j], operations[k])
        d = evaluate(m[i][k], m[k + 1][j], operations[k])

        minimum = min(minimum, a, b, c, d)
        maximum = max(maximum, a, b, c, d)

    return minimum, maximum


def find_maximum_value(dataset):
    assert 1 <= len(dataset) <= 29

    numbers, operations = list(map(int,dataset[::2])),dataset[1::2] # get numbers and operations from provided string input
    n = len(numbers)
    # two matrices store minimum and maximum numbers
    m = [[None for x in range(n)] for x in range(n)]
    M = [[None for x in range(n)] for x in range(n)]

    for i in range(n):
        m[i][i] = numbers[i]
        M[i][i] = numbers[i]

    for s in range(1, n):
        for i in range(1, n - s):
            j = i + s
            m[i][j], M[i][j] = min_and_max(M, m, i, j, operations)

    return M[0][n-1]

if __name__ == "__main__":
    print(find_maximum_value(input()))
