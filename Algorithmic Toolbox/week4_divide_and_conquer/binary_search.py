'''
Date: 2020-10-10 01:29:29
LastEditors: Cancan Huang @ Brown University
LastEditTime: 2020-10-12 14:05:33
'''
# Uses python3
import sys


def binary_search(a, x):
    left, right = 0, len(a)
    # write your code here
    while left < right:
        mid = int((left + right) / 2)
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    # data = [5, 1, 5, 8, 12, 13, 5, 8, 1, 23, 1, 11]
    n = data[0]
    m = data[n + 1]
    a = data[1: n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        # print(linear_search(a, x), end = ' ')
        print(binary_search(a, x), end=' ')
