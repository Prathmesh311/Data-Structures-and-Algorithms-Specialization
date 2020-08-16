# Uses python3

import sys


# Method 1 using marking number
def explore(i, adj, visited, cc, ccnum):
    visited[i] = 1
    ccnum[i] = cc
    for j in adj[i]:
        if visited[j] == 0:
            explore(j, adj, visited, cc, ccnum)


def reach(adj):
    # write your code here
    visited = [0] * (len(adj) + 1)
    ccnum = [0] * (len(adj) + 1)
    cc = 1
    for i in range(0, len(adj)):
        if visited[i] == 0:
            explore(i, adj, visited, cc, ccnum)
            cc = cc + 1

    result = []
    for k in range(0, len(ccnum)):
        if ccnum[k] not in result and ccnum[k] != 0:
            result.append(ccnum[k])

    return len(result)


# Method 2 using temperary list
def explore1(i, adj, visited, temp):
    visited[i] = 1
    temp.append(i)
    for j in adj[i]:
        if visited[j] == 0:
            temp = explore1(j, adj, visited, temp)
    return temp


def reach1(adj):
    # write your code here
    visited = [0] * (len(adj) + 1)
    cc = []

    for i in range(0, len(adj)):
        if visited[i] == 0:
            temp = []
            cc.append(explore1(i, adj, visited, temp))

    return len(cc)


def number_of_components(adj):
    result = 0
    # write your code here
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    # print(data)
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    # print(number_of_components(adj))
    print(reach(adj))
