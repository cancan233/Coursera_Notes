# Uses python3

import sys


def lcs2(a, b):
    # write your code here
    m, n = len(a), len(b)
    D = [[0 for j in range(n + 1)] for i in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                D[i][j] = 0
            elif a[i - 1] == b[j - 1]:
                D[i][j] = D[i - 1][j - 1] + 1
            else:
                D[i][j] = max(D[i - 1][j], D[i][j - 1])
    return D[m][n]


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
