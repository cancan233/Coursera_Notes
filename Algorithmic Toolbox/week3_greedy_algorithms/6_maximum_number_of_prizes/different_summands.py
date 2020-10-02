"""
Author: Cancan Huang
Date: 2020-09-22 21:30:19
"""
# Uses python3
import sys
import random


def optimal_summands(n):
    summands = []
    # write your code here
    used = 0
    i = 1
    while 1:
        summands.append(i)
        used = used + i
        if i >= (n - used):
            used = used - i
            break
        i += 1
    del summands[i - 1]
    summands.append(n - used)
    return summands


if __name__ == "__main__":
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=" ")
