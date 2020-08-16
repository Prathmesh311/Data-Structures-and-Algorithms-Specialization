# Uses python3

import sys

sys.setrecursionlimit(200000)


def dfs_forward(i, visited, adj, stack):
    visited[i] = 1

    for j in adj[i]:
        if visited[j] == 0:
            stack = dfs_forward(i, visited, adj, stack)

    stack.insert(0, i)
    return stack


def add_edge(transpose, adj, destination):
    transpose[adj].append(destination)


def graph_reverse(adj, transpose):

    for i in range(len(adj)):
        for j in range(len(adj[i])):
            add_edge(transpose, adj[i][j], i)

    return transpose


def dfs_reverse(curr_node, visited, transpose, stack, temp):
    visited[curr_node] = 1
    temp.append(curr_node)

    for i in transpose[curr_node]:
        if visited[i] == 0:
            temp = dfs_reverse(curr_node, visited, transpose, stack, temp)

    return temp


def number_of_strongly_connected_components(adj):
    result = []
    # write your code here
    # print(adj)
    visited = [0] * len(adj)
    stack = []

    for i in range(len(adj)):
        if visited[i] == 0:
            stack = dfs_forward(i, visited, adj, stack)
    # print(stack)
    visited = [0] * len(adj)
    transpose = [[] for i in range(len(adj))]
    transpose = graph_reverse(adj, transpose)
    # print(transpose)
    while len(stack) != 0:
        curr_node = stack.pop(0)
        print(curr_node)
        if visited[curr_node] == 0:
            temp = []
            result.append(dfs_reverse(curr_node, visited, transpose, stack, temp))
    # print(result)
    return len(result)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
