"""Consider you have a list of integers and a number n, find a pairs of elements which are sum equal to n and
    a pairs are unique, (a, b) is equal to (b, a)
Example:
n = 10
nums = [1, 3, 5, 6, 3, 4, 5, 7, 2, 2]

expected = [(3, 7), (5,5), (6,4)]
"""

inputs = [
    {
        'n': 10,
        'nums': [1, 3, 5, 6, 3, 4, 5, 7, 7, 7, 2, 2],
    },
    {
        'n': 10,
        'nums':  [8, 7, 2, 5, 3, 1],
    },
]


def find_pairs_of_sum_sort(n: int, nums: list) -> list:
    result = []

    temp_num = nums.copy()
    temp_num.sort()
    low, high = 0, len(temp_num) - 1

    while low < high:
        if temp_num[low] + temp_num[high] == n:
            result.append((temp_num[low], temp_num[high]))
            low += 1
            high -= 1
        elif temp_num[low] + temp_num[high] < n:
            low += 1
        else:
            high -= 1
    return set(result)


def find_pairs_of_sum_dict(n: int, nums: list) -> list:
    temp_dict = {}

    for i in nums:
        e = n - i
        if i not in temp_dict and e in nums and e not in temp_dict:
            temp_dict[i] = e
    result = [(k, v) for k, v in temp_dict.items()]
    return result


if __name__ == "__main__":
    for input_data in inputs:
        print('Input: ')
        print(f'- n={input_data["n"]}')
        print(f'- nums={input_data["nums"]}')
        print('Output: ')
        result = find_pairs_of_sum_sort(input_data['n'], input_data['nums'])
        print(f'- find_pairs_of_sum_sort {result}')
        result = find_pairs_of_sum_dict(input_data['n'], input_data['nums'])
        print(f'- find_pairs_of_sum_dict {result}')
        print('-' * 80)
