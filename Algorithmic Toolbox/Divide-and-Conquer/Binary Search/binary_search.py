# python3


def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1


def binary_search(a, x):
    left, right = 0, (len(a) - 1)
    return binary_search_run(a, left, right, x)


def binary_search_run(a, left, right, x):
    if right < left:
        return -1
    mid = int(left + (right - left) / 2)
    if x == a[mid]:
        return mid
    elif x > a[mid]:
        return binary_search_run(a, mid + 1, right, x)
    else:
        return binary_search_run(a, left, mid - 1, x)


def binary_search2(keys, query):
    assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
    assert 1 <= len(keys) <= 3 * 10 ** 4

    left, right = 0, len(keys) - 1

    while left <= right:
        mid = (right - 1 + left) // 2
        if mid < len(keys):
            if keys[mid] == query:
                return mid
            elif query < keys[mid]:
                right = mid - 1
            else:
                left = mid + 1

    return -1


if __name__ == '__main__':
    input_keys = list(map(int, input().split()))[1:]
    input_queries = list(map(int, input().split()))[1:]

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
