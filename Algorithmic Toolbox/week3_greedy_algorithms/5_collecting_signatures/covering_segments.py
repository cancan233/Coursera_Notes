"""
Author: Cancan Huang
Date: 2020-09-22 20:35:59
"""
# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple("Segment", "start end")


def optimal_points(segments):
    points = []
    # write your code here
    segments = sorted(segments, key=lambda s: s[1])
    while len(segments) > 0:
        min_right = segments[0].end
        points.append(min_right)
        i = 0
        while i < len(segments):
            if segments[i].start <= min_right and min_right <= segments[i].end:
                del segments[i]
            else:
                i += 1
    return points


if __name__ == "__main__":
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
