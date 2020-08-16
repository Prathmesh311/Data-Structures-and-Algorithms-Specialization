# python3


def left_child(i):
    return 2 * i + 1


def right_child(i):
    return 2 * i + 2


def min_heapify(H, i, swaps):
    l = left_child(i)
    r = right_child(i)
    min_index = i

    if l <= len(H) and H[l] < H[min_index]:
        min_index = l

    if r <= len(H) and H[r] < H[min_index]:
        min_index = r

        if i != min_index:
            swaps.append((i, min_index))
            H[i], H[min_index] = H[min_index], H[i]
            swaps = min_heapify(H, min_index, swaps)

    return swaps


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation

    heap_size = len(data)
    swaps = []

    '''swaps.append((3,4))
    print(swaps)'''
    if heap_size % 2 == 0:
        starts = (heap_size // 2) - 1
    else:
        starts = heap_size // 2

    for i in range(starts, 0):
        swaps = min_heapify(data, i, swaps)

    return swaps


def build_heap1(data):
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
