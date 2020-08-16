# python3
import sys


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

    def Max(self):
        assert (len(self.__stack))
        return max(self.__stack)


if __name__ == '__main__':
    stack = StackWithMax()
    maxStack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            x = int(query[1])
            stack.Push(x)
            if len(maxStack) == 0:
                maxStack.Push(x)

            y = maxStack.Peep()
            if x >= y:
                maxStack.Push(x)

        elif query[0] == "pop":
            top = stack.Pop()

            y = maxStack.Peep()
            if top == y:
                maxStack.Pop()

        elif query[0] == "max":
            print(maxStack.Peep())
            # print(stack.Max())
        else:
            assert (0)
