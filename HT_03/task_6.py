# Write a script to get the maximum and minimum value in a dictionary.

def value_len(v):
    try:
        iter(v)
        return len(v)
    except TypeError:
        return v


def get_key(d: dict, v):
    for k in d:
        if d[k] == v:
            return k


test_dict = {1: 100, 2: 10, 3: 110, 4: 6, 5: 'string', 6: [1, 2, 4], 7: (1, 2, 4)}
d_copy = test_dict.copy()
for key, value in test_dict.items():
    d_copy[key] = value_len(value)

print(test_dict)
lst_values = list(d_copy.values())
print(f'Minimum value in the dictionary: {get_key(d_copy, min(lst_values))}:{min(lst_values)}')
print(f'Maximum value in the dictionary: {get_key(d_copy, max(lst_values))}:{max(lst_values)}')
