#Uses python3

import sys


def negative_cycle(adj, cost):
    # write your code here
    dist = [9223372036854775807] * len(adj)

    # prev = [None] * len(adj)         -- prev used to keep track of previous elements to find shortest path afterwards

    dist[0] = 0
    for _ in range(len(adj) - 1):
        for j in range(len(adj)):
            i = 0
            for v in adj[j]:
                weight = dist[j] + cost[j][i]
                if dist[v] > weight:
                    dist[v] = weight
                    # prev[v] = j
                else:
                    i += 1

    for j in range(len(adj)):
        i = 0
        for v in adj[j]:
            weight = dist[j] + cost[j][i]
            if dist[v] > weight:
                return 1
            else:
                i += 1

    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))


