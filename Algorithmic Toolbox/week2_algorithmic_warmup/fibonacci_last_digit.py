"""
Author: Cancan Huang
Date: 2020-09-16 23:04:23
LastEditTime: 2020-09-16 23:04:24
"""
# Uses python3
import sys


def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


def get_fibonacci_last_digit_fast(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10

    return current % 10


if __name__ == "__main__":
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_fast(int(input)))
