# python3


class BuildHeap:

    def __init__(self):
        self.swaps = []
        self.data = []
        self.size = 0

    def reading(self):
        n = int(input())
        self.data = list(map(int, input().split()))
        self.size = len(self.data) - 1
        assert len(self.data) == n

    def printing(self):
        print(len(self.swaps))
        for s in self.swaps:
            print(s[0], s[1])

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def min_heapify(self, i):

        l = self.left_child(i)
        r = self.right_child(i)
        min_index = int(i)
        # print(l)
        # print(r)
        if l <= len(self.data) - 1 and self.data[l] < self.data[min_index]:
            min_index = l
        if r <= len(self.data) - 1 and self.data[r] < self.data[min_index]:
            min_index = r

        if i != min_index:
            self.swaps.append((int(i), min_index))
            self.data[int(i)], self.data[min_index] = self.data[min_index], self.data[int(i)]
            # print(self.swaps)
            self.min_heapify(min_index)

    def build_heap(self):
        heap_size = len(self.data) - 1

        if heap_size % 2 == 0:
            starts = (heap_size // 2) - 1
        else:
            starts = heap_size // 2

        for i in range(starts, -1, -1):
            self.min_heapify(i)

    def heap_sort(self):
        self.calculation()

        for i in range(0, len(self.data)):
            self.data[i], self.data[self.size] = self.data[self.size], self.data[i]
            self.size = self.size - 1
            self.min_heapify(0)

    def calculation(self):
        self.reading()
        self.build_heap()
        self.printing()


if __name__ == '__main__':
    b1 = BuildHeap()
    # b1.heap_sort()
    b1.calculation()
