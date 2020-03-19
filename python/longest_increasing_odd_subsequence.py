"""Given an array of integers, find the longest increasing sub array which contains odd numbers
"""

inputs = [
    [1, 3, 2, 1, 5, 7, 5, 1, 3, 4, 7, 9, 11, 13],
    [1, 3, 2, 1, 5, 7, 5, 1, 3, 4, 7, 9, 11, 13, 20],
    [],
    [2, 4, 6],
    [1],
    [1, 11],
]


def lis(list_numbers: list) -> list:
    if not list_numbers:
        return []

    list_length = len(list_numbers)
    if list_length == 1:
        if list_numbers[0] % 2 == 1:
            return list_numbers
        else:
            return []

    length = 0
    max_length = 0
    begin_index = 0

    length += (list_numbers[0] % 2)

    for i in range(1, list_length):
        if list_numbers[i] % 2 == 1 and list_numbers[i-1] <= list_numbers[i]:
            if length == 0:
                begin_index = i
            length += 1
        else:
            if max_length < length:
                max_length = length
            length = 0
    if max_length < length:
        max_length = length
    if max_length < 1:
        return []
    return list_numbers[begin_index:begin_index+max_length]


if __name__ == "__main__":
    for input_data in inputs:
        print(f'Input: {input_data}')
        print(f'Output: {lis(input_data)}')
