# Uses python3

import sys
from queue import Queue
# import queue


# BFS using queue liabrary
def distance(adj, s, t):
    # write your code here
    dist = [-1] * len(adj)
    dist[s] = 0

    q = Queue()
    q.put(s)

    while q:
        curr_node = q.get()
        for i in adj[curr_node]:
            if dist[i] == -1:
                q.put(i)
                dist[i] = dist[curr_node] + 1

    return dist[t]


# BFS using list as a queue
def distance1(adj, s, t):
    # write your code here
    dist = [-1] * len(adj)
    dist[s] = 0

    queue = []
    queue.append(s)

    while queue:
        curr_node = queue.pop(0)
        for i in adj[curr_node]:
            if dist[i] == -1:
                queue.append(i)
                dist[i] = dist[curr_node] + 1

    return dist[t]


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
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance1(adj, s, t))


