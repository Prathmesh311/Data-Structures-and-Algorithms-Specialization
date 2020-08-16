# Uses python3

import sys
# import queue


def bipartite(adj):
    # write your code here
    dist = [-1] * len(adj)
    dist[0] = 0

    queue = []
    queue.append(0)
    max_dist = 0

    while queue:
        curr_node = queue.pop(0)
        for i in adj[curr_node]:
            if dist[i] == -1:
                queue.append(i)
                dist[i] = dist[curr_node] + 1
                if max_dist < dist[i]:
                    max_dist = dist[i]

    # This method is accurate but slow
    for i in range(max_dist, 0, -1):  # loop through distance
        for j in range(len(adj)):     # loop through all vertex
            if dist[j] == i:
                for k in adj[j]:      # loop through edges for vertex matching distance with 1 st for loop
                    if dist[k] == i:
                        return 0

    return 1


def bipartite1(adj):
    # write your code here
    dist = [-1] * len(adj)
    dist[0] = 0

    queue = []
    queue.append(0)
    # max_dist = 0

    while queue:
        curr_node = queue.pop(0)
        for i in adj[curr_node]:
            if dist[i] == -1:
                queue.append(i)
                dist[i] = dist[curr_node] + 1

            for j in adj[i]:
                if j in adj[curr_node] or j in adj[last_elem]:
                    return 0
            last_elem = i
    return 1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite1(adj))
