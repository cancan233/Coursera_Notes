"""
Author: Cancan Huang
Date: 2020-09-17 00:14:22
LastEditTime: 2020-09-17 00:14:23
"""
# Uses python3
import sys


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10


def Pisanoperiod(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m
        if previous == 0 and current == 1:
            return i + 1


def fibonacci_sum_fast(n):
    if n <= 1:
        return n

    pisano_period = Pisanoperiod(10)
    previous, current, sum = 0, 1, 1
    n = n % pisano_period
    for i in range(1, pisano_period):
        previous, current = current, (previous + current) % 10
        sum = (sum + current) % 10
        if i == (n - 1):
            n_sum = sum
    return (sum * pisano_period + n_sum) % 10


if __name__ == "__main__":
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_fast(n))
