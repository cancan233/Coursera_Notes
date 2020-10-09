"""
Author: Cancan Huang
Date: 2020-09-17 01:09:13
LastEditTime: 2020-09-17 01:09:24
"""

# Uses python3
import random
import numpy as np


def calc_fib(n):
    if n <= 1:
        return n
    else:
        return calc_fib(n - 1) + calc_fib(n - 2)


def calc_fib_direct(n):
    if n <= 1:
        return n
    else:
        previous, current = 0, 1
        for i in range(n - 1):
            previous, current = current, previous + current
        return current


def calc_fib_fast(n):
    if n <= 1:
        return n
    else:
        F = np.zeros(n + 1, dtype=int64)
        F[0] = 0
        F[1] = 1
        for i in range(2, n + 1):
            F[i] = F[i - 1] + F[i - 2]
        return int(F[n])


def calc_fib_matrix(n):
    v1, v2, v3 = 1, 1, 0  # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[
        3:
    ]:  # (binary exponentiation) perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2 * v2
        v1, v2, v3 = v1 * v1 + calc, (v1 + v3) * v2, calc + v3 * v3
        if rec == "1":
            v1, v2, v3 = v1 + v2, v1, v2
    return v2


# n = int(input())
n = 100
print(calc_fib_matrix(n))
# print(calc_fib_direct(n))
# print(calc_fib_fast(n))
