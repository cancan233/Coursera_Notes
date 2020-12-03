# Uses python3
import sys


def get_change(m):
    # write your code here
    if m < 0:
        return 0
    else:
        MinNumCoins = [0 for i in range(m + 1)]
        for i in range(1, m + 1):
            MinNumCoins[i] = float("inf")
            for change in [1, 3, 4]:
                if i >= change:
                    NumCoins = MinNumCoins[i - change] + 1
                    if NumCoins < MinNumCoins[i]:
                        MinNumCoins[i] = NumCoins
    return MinNumCoins[m]


if __name__ == "__main__":
    m = int(sys.stdin.read())
    print(get_change(m))
