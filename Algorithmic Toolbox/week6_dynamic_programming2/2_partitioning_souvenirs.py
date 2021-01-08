# Uses python3
import sys
import itertools


def partition3(A):
    # for c in itertools.product(range(3), repeat=len(A)):
    #     sums = [None] * 3
    #     for i in range(3):
    #         sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

    #     if sums[0] == sums[1] and sums[1] == sums[2]:
    #         return 1

    # return 0

    if len(A) < 3:
        return 0
    elif sum(A) % 3 != 0:
        return 0
    else:
        W = sum(A) // 3
        count = 0
        value = [[0 for j in range(len(A) + 1)] for i in range(W + 1)]
        for i in range(1, W + 1):
            for j in range(1, len(A) + 1):
                value[i][j] = value[i][j - 1]
                if A[j - 1] <= i:
                    temp = value[i - A[j - 1]][j - 1] + A[j - 1]
                    if temp > value[i][j]:
                        value[i][j] = temp
                if value[i][j] == W:
                    count += 1
        if count < 3:
            return 0
        else:
            return 1


if __name__ == "__main__":
    # input = sys.stdin.read()
    input = "4 4 1 3 2"
    n, *A = list(map(int, input.split()))
    print(partition3(A))
