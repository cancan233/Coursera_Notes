# python3


def max_pairwise_product(numbers):
    if numbers[0] > numbers[1]:
        first_number = numbers[0]
        second_number = numbers[1]
    else:
        first_number = numbers[1]
        second_number = numbers[0]
    for i in range(2, len(numbers)):
        if numbers[i] >= second_number:
            second_number = numbers[i]
        if numbers[i] >= first_number:
            second_number = first_number
            first_number = numbers[i]
    max_product = first_number * second_number
    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]

    print(max_pairwise_product(input_numbers))
