#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


def IsBinarySearchTree(j, mn, mx):
    # Implement correct algorithm here
    if not j in tree:
        return True

    if tree[j][0] < mn or tree[j][0] > mx:
        return False

    return IsBinarySearchTree(tree[j][1], mn, tree[j][0] - 1) and IsBinarySearchTree(tree[j][2], tree[j][0], mx)



def main():
    nodes = int(sys.stdin.readline().strip())
    global tree
    tree, mn, mx = {}, -2147483647, 2147483647
    for i in range(nodes):
        tree[i] = (list(map(int, sys.stdin.readline().strip().split())))
    if IsBinarySearchTree(0, mn ,mx):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
