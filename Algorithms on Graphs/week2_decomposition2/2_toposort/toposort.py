# Uses python3

import sys


def dfs(adj, used, order, x):
    # write your code here
    used[x] = 1

    for j in adj[x]:
        if used[j] == 0:
            order = dfs(adj, used, order, j)

    order.append(x)
    return order


def toposort(adj):
    # print(adj)
    used = [0] * len(adj)
    order = []
    # write your code here
    for i in range(len(adj)):
        if used[i] == 0:
            order = dfs(adj, used, order, i)

    return reversed(order)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')


