# Uses python3

import sys


def explore(i, adj, visited):
    visited[i] = 1

    for j in adj[i]:
        if visited[j] == 0:
            explore(j, adj, visited)


def reach(adj, x, y):
    # write your code here
    visited = [0] * (len(adj) + 1)

    explore(x, adj, visited)

    if visited[x] == 1 and visited[y] == 1:
        return 1

    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    # print(data)
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    # print(edges)
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)

    result = reach(adj, x, y)
    print(result)
