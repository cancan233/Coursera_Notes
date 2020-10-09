"""
Author: Cancan Huang
Date: 2020-09-16 23:08:17
LastEditTime: 2020-09-16 23:08:18
"""
# Uses python3
import sys


def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            current_gcd = d

    return current_gcd


def gcd_fast(a, b):
    while 1:
        a, b = b, a % b
        if b == 0:
            break
        gcd_fast(a, b)

    return a


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    if a >= b:
        print(gcd_fast(a, b))
    else:
        print(gcd_fast(b, a))
