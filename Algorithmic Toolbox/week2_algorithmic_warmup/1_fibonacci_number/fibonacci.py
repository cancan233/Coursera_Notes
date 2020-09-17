"""
Author: Cancan Huang
Date: 2020-09-17 00:50:49
LastEditTime: 2020-09-17 00:50:49
"""
"""
Author: Cancan Huang
Date: 2020-09-16 22:48:53
LastEditTime: 2020-09-17 00:07:30
"""
# Uses python3
import random
import numpy as np


def calc_fib(n):
    if n <= 1:
        return n
    else:
        return calc_fib(n - 1) + calc_fib(n - 2)


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


# n = int(input())
n = 100
print(calc_fib(n))
print(calc_fib_fast(n))
