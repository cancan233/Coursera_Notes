"""
Author: Cancan Huang
Date: 2020-09-22 14:05:52
"""
# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    refills = 0
    current_stop = 0
    stops = [0] + stops + [distance]
    for i in range(len(stops)):
        if stops[current_stop] + tank < stops[i]:
            refills += 1
            current_stop = i - 1
        if stops[current_stop] + tank == stops[i] and stops[i] != distance:
            refills += 1
            current_stop = i
        if stops[i - 1] + tank < stops[i]:
            return -1
        if stops[i] == distance:
            return refills


if __name__ == "__main__":
    d, m, _, *stops = map(int, sys.stdin.read().split())
    # d, m, _, *stops = 1, 1, 1, 0
    print(compute_min_refills(d, m, stops))
