# python3


def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums


class queue():
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, x):

        while len(self.s1) != 0:
            self.s2.append(self.s1[-1])
            self.s1.pop()

        self.s1.append(x)

        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()

    def dequeue(self):
        if len(self.s1) == 0:
            print("Q is empty")

        x = self.s1[-1]
        self.s1.pop()
        return x

    def Max(self):
        return max(self.s1)


class StackWithMax():
    def __init__(self):
        self.__stack = []

    def Push(self, a):
        self.__stack.append(a)

    def Pop(self):
        assert (len(self.__stack))
        return self.__stack.pop()

    def Peep(self):
        n = len(self.__stack)
        return self.__stack[n - 1]

    def __len__(self):
        return len(self.__stack)

    def empty(self):
        while len(self.__stack) != 0:
            self.__stack.pop()

    def Max(self):
        assert (len(self.__stack))
        return max(self.__stack)


def max_sliding_window(sequence, m):
    q = queue()
    maxstack = StackWithMax()
    secondLargest = StackWithMax()
    maximum = []

    index = 0
    for k in range(0, m):
        q.enqueue(sequence[k])
        if len(maxstack) == 0:
            maxstack.Push(sequence[k])
        else:
            y = maxstack.Peep()
            if sequence[k] > y:
                maxstack.Push(sequence[k])
            else:
                if len(secondLargest) == 0:
                    secondLargest.Push(sequence[k])
                    index = k
                else:
                    z = secondLargest.Peep()
                    if sequence[k] > z:
                        secondLargest.Push(sequence[k])
                        index = k

    maximum.append(maxstack.Peep())

    for i in range(m, len(sequence)):
        # check = 0
        curr_pop_value = q.dequeue()

        if curr_pop_value == maxstack.Peep():
            maxstack.Pop()
            q.enqueue(sequence[i])

            if len(secondLargest) == 0:
                maxstack.Push(q.Max())
            else:
                if sequence[i] > secondLargest.Peep():
                    maxstack.Push(sequence[i])
                else:
                    maxstack.Push(secondLargest.Peep())
                    secondLargest.Pop()
        else:
            q.enqueue(sequence[i])
            if len(maxstack) == 0:
                maxstack.Push(secondLargest.Peep())
                secondLargest.Pop()
            else:
                y = maxstack.Peep()
                if sequence[i] > y:
                    maxstack.Push(sequence[i])
                else:
                    if len(secondLargest) == 0:
                        secondLargest.Push(sequence[i])
                        index = i
                    else:
                        z = secondLargest.Peep()
                        if sequence[i] > z:
                            secondLargest.Push(sequence[i])
                            index = i

        if len(secondLargest) != 0 and  (i - index) % m == 1:
            secondLargest.empty()
        maximum.append(maxstack.Peep())


    return maximum


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window(input_sequence, window_size))
