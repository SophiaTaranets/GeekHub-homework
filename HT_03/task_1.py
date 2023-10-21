# Write a script that will run through a list of tuples and replace the last value for each tuple.
# The list of tuples can be hardcoded. The "replacement" value is entered by user.
# The number of elements in the tuples must be different.

# Tuples for the test
# t = (2023, 'geekhub', True, 12)
# t = (2023, 'geekhub', True, 12, 15.5)
# t = (2023, 'geekhub', True, 12, 15.5, [1, 2, 3])
# t = (2023, 'geekhub', True, 12, 15.5, (1, 2, 3))
# t = (2023, 'geekhub', True, 12, 15.5, {1: 1})
t = (2023, 'geekhub', True, 12, 15.5, [1, 2, 3], 'string')
lst = list(t)

print('Some rules to use the program:\n'
      '1 - You can replace elements only with similar type\n'
      '2 - If type of the last elements is the collection like '
      'list, tuple or set you should enter elements with separator " "\n'
      '3 - If type of the last elements is "dict" you should enter elements this format:'
      'key1:value1,key2:value2,')
print(f'Consider the type of last value in current tuple is {type(lst[-1])}')

new_value = input('Enter last value: ')
try:
    if isinstance(lst[-1], bool):
        lst[-1] = bool(new_value)
    elif isinstance(lst[-1], int):
        lst[-1] = int(new_value)
    elif isinstance(lst[-1], float):
        lst[-1] = float(new_value)
    elif isinstance(lst[-1], str):
        lst[-1] = new_value
    elif isinstance(lst[-1], list):
        lst[-1] = new_value.split(' ')
    elif isinstance(lst[-1], tuple):
        lst[-1] = tuple(new_value.split(' '))
    elif isinstance(lst[-1], set):
        lst[-1] = set(new_value.split(' '))
    elif isinstance(lst[-1], dict):
        d = {}
        s = new_value.split(',')
        for i in s:
            k = i.split(':')
            d[k[0]] = k[1]
        lst[-1] = d
    else:
        last_value = new_value
except Exception as e:
    print(e)

print(f'Changed tuple: {tuple(lst)}')
