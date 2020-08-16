# python3
from operator import itemgetter
from operator import attrgetter

from collections import namedtuple
from sys import stdin

Segment = namedtuple('Segment', 'start end')


def compute_optimal_points(segments):


    points = []
    segments = sorted(segments, key=attrgetter('end'))
    curr_right_end = segments[0].end
    points.append(curr_right_end)
    i = 1
    while i < len(segments):
        if curr_right_end < segments[i].start:
            curr_right_end = segments[i].end
            points.append(curr_right_end)
        i += 1


    return points


if __name__ == '__main__':
    n, *data = map(int, stdin.read().split())
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    assert n == len(input_segments)
    output_points = compute_optimal_points(input_segments)
    print(len(output_points))
    print(*output_points)
