# Uses python3
import sys


def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    # write your code here
    left_majority_element = get_majority_element(a, left, (left + right - 1) // 2)
    right_majority_element = get_majority_element(a, (left + right - 1) // 2 + 1, right)

    left_count, right_count = 0, 0
    for i in range(left, right):
        if a[i] == left_majority_element:
            left_count += 1
        if left_count > (right - left) / 2:
            return left_majority_element
    for i in range(left, right):
        if a[i] == right_majority_element:
            right_count += 1
        if right_count > (right - left) / 2:
            return right_majority_element

    return -1


if __name__ == "__main__":
    input = sys.stdin.read()
    # input = "10 2 124554847 2 941795895 2 2 2 2 792755190 756617003"
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
