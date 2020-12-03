# Uses python3
import sys


def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)


def DP_optimal_sequence(n):
    if n == 0:
        return [-1]
    else:
        parents = [0 for i in range(n + 1)]
        MinNumOp = [0 for i in range(n + 1)]
        for i in range(1, n + 1):
            curr_parent = i - 1
            curr_NumOp = MinNumOp[curr_parent] + 1

            if i % 3 == 0:
                parent = i // 3
                NumOp = MinNumOp[parent] + 1
                if NumOp < curr_NumOp:
                    curr_parent, curr_NumOp = parent, NumOp

            if i % 2 == 0:
                parent = i // 2
                NumOp = MinNumOp[parent] + 1
                if NumOp < curr_NumOp:
                    curr_parent, curr_NumOp = parent, NumOp

            parents[i], MinNumOp[i] = curr_parent, curr_NumOp

        sequence = []
        k = n
        while k > 0:
            sequence.append(k)
            k = parents[k]
        sequence.reverse()
        return sequence


input = sys.stdin.read()
n = int(input)
sequence = list(DP_optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=" ")
