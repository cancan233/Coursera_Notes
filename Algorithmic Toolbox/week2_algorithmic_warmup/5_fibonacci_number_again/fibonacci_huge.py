"""
Author: Cancan Huang
Date: 2020-09-16 23:47:37
LastEditTime: 2020-09-16 23:47:37
"""
# Uses python3
import sys
import numpy as np


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def Pisanoperiod(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m
        if previous == 0 and current == 1:
            return i + 1


def calc_fib_fast(n):
    if n <= 1:
        return n
    else:
        F = np.zeros(n + 1)
        F[0] = 0
        F[1] = 1
        for i in range(2, n + 1):
            F[i] = F[i - 1] + F[i - 2]
        return int(F[n])


def get_fibonacci_huge_fast(n, m):
    pisano_period = Pisanoperiod(m)
    n = n % pisano_period
    # if n <= 1:
    #     return n
    # current = calc_fib_fast(n)

    previous, current = 0, 1
    if n <= 1:
        return n
    for i in range(n - 1):
        previous, current = current, previous + current

    return current % m


if __name__ == "__main__":
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge_fast(n, m))
