"""
Author: Cancan Huang
Date: 2020-09-22 22:47:23
"""
# Uses python3

import sys
import math


def largest_number(a):
    # write your code here
    res = ""
    while a:
        maxdigit = "0"
        for i in range(len(a)):
            if int(a[i] + maxdigit) > int(maxdigit + a[i]):
                maxdigit = a[i]
                max_i = i
        res += maxdigit
        del a[max_i]
    return res


if __name__ == "__main__":
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
