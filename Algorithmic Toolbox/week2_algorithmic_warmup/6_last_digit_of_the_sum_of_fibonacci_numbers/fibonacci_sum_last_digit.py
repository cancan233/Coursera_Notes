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


### F0 + F1 + F2 + ... + Fn = F(n+2) - 1
def fibonacci_sum_fast(n):
    pisano_period = Pisanoperiod(10)
    previous, current = 0, 1
    if n <= 2:
        return n
    # if n == 2:
    #     return 3
    n = (n + 2) % pisano_period
    for i in range(n - 1):
        previous, current = current, (previous + current) % 10
    return (current + 9) % 10


if __name__ == "__main__":
    input = sys.stdin.read()
    n = int(input)
    # n = 3
    print(fibonacci_sum_fast(n))
