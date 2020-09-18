"""
Author: Cancan Huang
Date: 2020-09-16 23:46:46
LastEditTime: 2020-09-17 19:31:22
"""
# Uses python3
from sys import stdin


def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10


def Pisanoperiod(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m
        if previous == 0 and current == 1:
            return i + 1


def fibonacci_sum_squares_fast(n):
    pisano_period = Pisanoperiod(10)
    n = n % pisano_period
    previous, current = 0, 1
    if n <= 1:
        return n
    for i in range(n):
        previous, current = current, (previous + current) % 10
    return (previous * current) % 10


if __name__ == "__main__":
    n = int(stdin.read())
    print(fibonacci_sum_squares_fast(n))
