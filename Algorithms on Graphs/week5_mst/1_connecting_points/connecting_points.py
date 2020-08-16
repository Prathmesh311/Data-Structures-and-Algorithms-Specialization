# Uses python3
import sys
import math


def distance(x1, x2, y1, y2):
    diff = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    return diff


def parent(x, y, union):
    for i in range(len(union)):
        if union[i][0] == y:
            union[i][0] = x

    return union


def length(x, y, union):
    for i in range(len(union)):
        if union[i][1] == y:
            union[i][1] = x

    return union


def minimum_distance(x, y):
    result = 0.
    # write your code here
    edges = []

    for i in range(len(x)):
        for j in range(i, len(x)):
            if i != j:
                edges.append([i, j, distance(x[i], x[j], y[i], y[j])])

    sorted_edges = sorted(edges, key=lambda x: x[2])

    union = [[x, 0] for x in range(len(x))]
    # union = [0] * len(x)
    min_dist = 0.
    for k in sorted_edges:
        if union[k[0]][0] != union[k[1]][0]:

            min_dist += k[2]
            if union[k[0]][1] > union[k[1]][1]:
                union = parent(union[k[0]][0], union[k[1]][0], union)
                union = length(union[k[0]][1], union[k[1]][1], union)
                # union[k[1]][1] = union[k[0]][1]
                # union[k[1]][0] = union[k[0]][0]

            elif union[k[0]][1] == union[k[1]][1]:
                union = parent(union[k[0]][0], union[k[1]][0], union)
                union = length(union[k[0]][1] + 1, union[k[1]][1], union)
                union = length(union[k[1]][1], union[k[0]][1], union)

                # union[k[1]][1] = union[k[0]][1] + 1
                # union[k[0]][1] = union[k[1]][1]
                # union[k[1]][0] = union[k[0]][0]
            else:
                union = parent(union[k[1]][0], union[k[0]][0], union)
                union = length(union[k[1]][1], union[k[0]][1], union)
                # union[k[0]][1] = union[k[1]][1]
                # union[k[0]][0] = union[k[1]][0]

    return min_dist


def distance1(v1, v2, x, y):
    return math.sqrt((x[v1] - x[v2]) ** 2 + (y[v1] - y[v2]) ** 2)


def minimum_distance1(x, y):
    # create edge list
    edges = []
    for i in range(n):
        for j in range(i, n):
            if i != j:
                edges.append([i, j, distance1(i, j, x, y)])

    # sort edges based on the distances
    sorted_Edges = sorted(edges, key=lambda x: x[2])

    # initialize disjoint data structure
    membership = range(n)

    # run Kruskal algorithm
    MST = []  # initialize minimum spanning tree
    minDist = 0
    for i in sorted_Edges:
        # make sure vertices are not already joined
        if membership[i[0]] != membership[i[1]]:
            # add edge
            MST.append(i)
            minDist += i[2]
            # join groups
            membership = list(map(lambda x: membership[i[0]] if x == membership[i[1]] else x, membership))

    return minDist


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
