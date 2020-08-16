# python3


def partition3(values):
    assert 1 <= len(values) <= 20
    assert all(1 <= v <= 30 for v in values)

    partitioning = []
    partitioning.append(0)
    i = 0
    status = 0
    for i in range(len(values)):
        rem = (values[i] + partitioning[i]) % 3
        partitioning.append(rem)

        if rem == 0:
            status = 1

    if status == 1:
        return 1

    return 0


if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))
