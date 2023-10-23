# Write a script that will run through a list of tuples and replace the last value for each tuple.
# The list of tuples can be hardcoded. The "replacement" value is entered by user.
# The number of elements in the tuples must be different.

list_of_tuples = [(), (99, ), (1, 2, 3), (1, 2, 3, 4)]
result_list = []
new_last_value = int(input('Enter new value for the last element: '))
for list_element in list_of_tuples:
    if list_element:
        list_element = list(list_element)
        last_index = len(list_element) - 1
        list_element[last_index] = new_last_value
        result_list.append(tuple(list_element))
    else:
        result_list.append(list_element)

print(f'Result: {result_list}')
