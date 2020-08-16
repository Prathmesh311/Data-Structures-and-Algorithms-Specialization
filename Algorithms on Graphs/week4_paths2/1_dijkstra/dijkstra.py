#Uses python3

import sys
import queue


def min_value(visited, dist):
    minimum = 9223372036854775807
    min_index = len(dist)

    for i in range(len(dist)):
        if not visited[min_index] and minimum > dist[i]:
            minimum = dist[i]
            min_index = i

    return min_index


def distance(adj, cost, s, t):
    # write your code here
    dist = [9223372036854775807] * (len(adj))
    visited = [False] * len(adj)
    # prev = [None] * len(adj)

    dist[s] = 0
    for k in range(len(adj) - 1):
        # curr_elem = H.get()
        curr_elem = min_value(visited, dist)
        if curr_elem == len(adj):
            break
        visited[curr_elem] = True
        j = 0
        for i in adj[curr_elem]:
            # i_index = adj[curr_elem].index(i)
            if not visited[curr_elem] and dist[i] > dist[curr_elem] + cost[curr_elem][j]:
                dist[i] = dist[curr_elem] + cost[curr_elem][j]
                # prev[i] = curr_elem
                j += 1

    if dist[t] == 9223372036854775807:
        return -1

    return dist[t]


class Dijkstra:
    def __init__(self, adj, cost):
        self.adj = [adj]
        self.cost = [cost]
        self.dist = [9223372036854775807] * (len(self.adj) + 1)
        self.prev = [None] * len(self.adj)

    def distance(self, s, t):

        self.dist[s] = 0

        for k in range(len(self.adj) - 1):
            curr_elem = min(self.dist)
            curr_index = self.dist.index(curr_elem)
            for i in self.adj[curr_elem]:
                i_index = self.adj[curr_elem].index(i)
                if self.dist[i] > self.dist[curr_elem] + self.cost[curr_elem][i_index]:
                    self.dist[i] = self.dist[curr_elem] + self.cost[curr_elem][i_index]
                    self.prev[i] = curr_elem
            self.dist[curr_index] = 9223372036854775807

        return self.dist[t]


# using Dictionary
def distance5(adj, cost, s, t):
    dist = [9223372036854775807] * len(adj)
    Q = {i : 9223372036854775807 for i in range(len(adj))}

    # print(Q)
    dist[s] = 0

    while len(Q) != 0:
        curr_elem = min(Q, key=Q.get)
        Q.pop(curr_elem)
        '''index = 0
        for number, name in Q.items():
            if name == curr_elem:
                Q.pop(number)
                break
                # index = number'''
        # Q.pop(index)

        for i in adj[curr_elem]:
            curr_index = adj[curr_elem].index(i)
            if dist[i] > dist[curr_elem] + cost[curr_elem][curr_index]:
                dist[i] = dist[curr_elem] + cost[curr_elem][curr_index]
                Q[i] = dist[curr_elem] + cost[curr_elem][curr_index]

    if dist[t] == 9223372036854775807:
        return -1
    return dist[t]


class Node:
    def __init__(self, index, distance):
        self.index = index
        self.distance = distance

    def __eq__(self, other):
        return self.distance == other.distance

    def __ne__(self, other):
        return self.distance != other.distance

    def __lt__(self, other):
        return self.distance < other.distance

    def __gt__(self, other):
        return self.distance > other.distance

    def __ge__(self, other):
        return self.distance >= other.distance

    def __le__(self, other):
        return self.distance <= other.distance


def distance6(adj, cost, s, t):
    dist = [1000000 for u in adj]
    dist[s] = 0
    h = queue.PriorityQueue()
    h.put(Node(s, dist[s]))

    while not h.empty():
        u = h.get()
        for v in adj[u.index]:
            if dist[v] > dist[u.index] + cost[u.index][adj[u.index].index(v)]:
                dist[v] = dist[u.index] + cost[u.index][adj[u.index].index(v)]
                h.put(Node(v, dist[v]))

    return dist[t] if dist[t] != 1000000 else -1


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
    s, t = data[0] - 1, data[1] - 1
    print(distance6(adj, cost, s, t))

    # dj = Dijkstra(adj, cost)
    # print(dj.distance(s, t))


