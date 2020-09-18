"""
Author: Cancan Huang
Date: 2020-09-17 19:28:43
LastEditTime: 2020-09-17 19:28:54
"""
# Uses python3
import sys


def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10


def Pisanoperiod(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m
        if previous == 0 and current == 1:
            return i + 1


def get_fibonacci_huge_fast(n):
    pisano_period = Pisanoperiod(10)

    previous, current = 0, 1
    if n <= 2:
        return n
    # if n == 2:
    #     return

    n = (n + 2) % pisano_period
    for i in range(n - 1):
        previous, current = current, (previous + current) % 10
    return (current + 9) % 10


### F0 + F1 + F2 + ... + Fn = F(n+2) - 1
def fibonacci_partial_sum_fast(from_, to):
    from_sum = get_fibonacci_huge_fast(max(from_ - 1, 0))
    to_sum = get_fibonacci_huge_fast(to)
    # print(from_sum, to_sum)
    return (to_sum - from_sum + 10) % 10


if __name__ == "__main__":
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    # from_, to = 1, 2
    print(fibonacci_partial_sum_fast(from_, to))