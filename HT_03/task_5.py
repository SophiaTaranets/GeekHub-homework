# Write a script to remove values duplicates from dictionary. Feel free to hardcode your dictionary.

dictionary = {1: 'value', 2: 'value', 3: 'value3', 4: 'value4', 5: 'value3'}
unique_values = {}
for key, value in dictionary.items():
    if value not in unique_values.values():
        unique_values[key] = value
print(f'Dict with unique values: {unique_values}')
