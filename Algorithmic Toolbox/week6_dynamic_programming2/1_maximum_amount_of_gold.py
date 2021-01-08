# Uses python3
import sys


def optimal_weight(W, w):
    # write your code here
    # result = 0
    # for x in w:
    #     if result + x <= W:
    #         result = result + x
    # return result
    # w = [0] + w
    # weight = [[0 for j in range(len(w))] for i in range(W + 1)]
    # for i in range(1, len(w)):
    #     for curr_W in range(1, W + 1):
    #         prev = weight[curr_W][i - 1]
    #         Val = weight[W - w[i]][i - 1] + w[i]
    #         if Val < curr_W:
    #             weight[curr_W][i] = max(Val, prev)
    #         else:
    #             weight[curr_W][i] = prev
    # return weight[-1][-1]

    value = [[0 for j in range(len(w) + 1)] for i in range(W + 1)]
    for i in range(1, W + 1):
        for j in range(1, len(w) + 1):
            value[i][j] = value[i][j - 1]
            if w[j - 1] <= i:
                temp = value[i - w[j - 1]][j - 1] + w[j - 1]
                if temp > value[i][j]:
                    value[i][j] = temp
    return value[W][len(w)]


if __name__ == "__main__":
    # input = sys.stdin.read()
    input = "20 4 5 7 12 18"
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
