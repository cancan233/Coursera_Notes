"""
Author: Cancan Huang
Date: 2020-09-22 15:03:36
LastEditTime: 2020-09-22 15:03:37
"""
"""
Author: Cancan Huang
Date: 2020-09-22 13:57:25
LastEditTime: 2020-09-22 13:57:41
"""
# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0.0
    # write your code here
    value_per_weight = [i / j for i, j in zip(values, weights)]
    sorted_value_per_wight = [
        i[0]
        for i in sorted(
            enumerate(value_per_weight),
            key=lambda x: x[1],
            reverse=True,
        )
    ]
    weights = [weights[i] for i in sorted_value_per_wight]
    values = [values[i] for i in sorted_value_per_wight]
    for i in range(len(weights)):
        if capacity == 0:
            return value
        a = min(weights[i], capacity)
        value += a * values[i] / weights[i]
        weights[i] -= a
        capacity -= a
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2 : (2 * n + 2) : 2]
    weights = data[3 : (2 * n + 2) : 2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
