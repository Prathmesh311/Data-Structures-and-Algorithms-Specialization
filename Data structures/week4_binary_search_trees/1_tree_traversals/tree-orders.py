# python3

import sys, threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    '''def smallest_elem(self):

        return smallest'''

    def inOrder(self, root):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        '''if self.left[root] != -1:
            self.result = self.inOrder(self.left[root])
            self.result.append(self.key[root])
            if self.right[root] != -1:
                self.result.append(self.right[root])'''


        return self.result

    def preOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that

        return self.result

    def postOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that

        return self.result


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    #print(" ".join(str(x) for x in tree.preOrder()))
    #print(" ".join(str(x) for x in tree.postOrder()))


threading.Thread(target=main).start()
