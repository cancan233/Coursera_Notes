"""
Author: Cancan Huang
Date: 2020-09-16 23:26:04
LastEditTime: 2020-09-16 23:41:26
"""
# Uses python3
import sys


def lcm_naive(a, b):
    for l in range(1, a * b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a * b


def gcd_fast(a, b):
    while 1:
        a, b = b, a % b
        if b == 0:
            break
        gcd_fast(a, b)

    return a


def lcm_fast(a, b):
    if a >= b:
        gcd = gcd_fast(a, b)
    else:
        gcd = gcd_fast(b, a)
    return int(a * b / gcd)


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_fast(a, b))
