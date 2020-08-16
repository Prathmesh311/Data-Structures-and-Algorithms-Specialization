# Uses python3

import sys


# using Stack method
def explore(i, visited, adj, temp, indicator):
    visited[i] = 1
    temp.insert(0, i)

    for j in adj[i]:
        if j in temp:
            return 1
        elif visited[j] == 0:
            indicator = explore(j, visited, adj, temp, indicator)

    temp.pop(0)
    return indicator


# using Array method
def explore2(i, visited, adj, stack):
    visited[i] = 1
    stack[i] = 1

    for j in adj[i]:
        if visited[j] == 0:
            if explore2(j, visited, adj, stack) == 1:
                return 1
        elif stack[j] == 1:
            return 1

    stack[i] = 0
    return 0


def acyclic(adj):
    # print(adj)
    visited = [0] * (len(adj) + 1)
    stack = [0] * (len(adj) + 1)
    result = 0
    for i in range(0, len(adj)):
        if visited[i] == 0:
            temp = []
            indicator = 0
            result = explore(i, visited, adj, temp, indicator)
            if result == 1:
                return 1
            # if explore2(i, visited, adj, stack) == 1:
            #  return 1

    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
