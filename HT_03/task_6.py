# Write a script to get the maximum and minimum value in a dictionary.

def find_min_max_strings(dict_data: dict):
    group_strings = [value for value in dict_data.values() if isinstance(value, str)]
    return f'Between Strings: min={min(group_strings)} max={max(group_strings)}'


def find_min_max_numbers(dict_data: dict):
    group_numbers = [value for value in dict_data.values() if isinstance(value, (int, float))]
    return f'Between Numbers: min={min(group_numbers)} max={max(group_numbers)}'


def find_min_max_collections(dict_data: dict):
    group_collections = [value for value in dict_data.values() if isinstance(value, (list, tuple, set))]
    min_collection = min(group_collections, key=lambda x: min(x))
    max_collection = max(group_collections, key=lambda x: max(x))
    return f'Between Collections: min={min_collection} max={max_collection}'


test_dict = {1: 100, 2: 10,
             3: 110.4,
             4: 6,
             5: 'string',
             6: [1, 2, 4],
             7: (1, 2, 4, 12),
             8: 'geekhub',
             9: [10, 20, 40]}

print(find_min_max_strings(test_dict))
print(find_min_max_numbers(test_dict))
print(find_min_max_collections(test_dict))
