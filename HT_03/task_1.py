# Write a script that will run through a list of tuples and replace the last value for each tuple.
# The list of tuples can be hardcoded. The "replacement" value is entered by user.
# The number of elements in the tuples must be different.

list_of_tuples = [(), (99, ), (1, 2, 3), (1, 2, 3, 4)]
result = []
value = int(input('Enter value: '))
for t in list_of_tuples:
    if len(t) == 0:
        result.append(t)
    else:
        t = list(t)
        last_index = len(t) - 1
        t[last_index] = value
        result.append(tuple(t))
print(result)
