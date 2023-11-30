# Create 'list'-like object, but index starts from 1 and index of 0 raises error.
# Тобто це повинен бути клас, який буде поводити себе так,
# як list (маючи основні методи), але індексація повинна починатись із 1

class MyList(list):
    def __getitem__(self, index):
        if index == 0:
            raise IndexError('Index start from 1')

        adjusted_index = index - 1
        return super().__getitem__(adjusted_index)


# Test list
test_list_1 = MyList(['item 1', 'item 2', 'item 3'])
test_list_2 = MyList(['item 1', 'item 2', 'item 3'])
try:
    print(test_list_1[0])
except IndexError as error:
    print(error)

print(f'First element: {test_list_1[1]}')
test_list_1.append(100)
test_list_1.extend([200, 300])
print(f'Append-Extend: {test_list_1}')
test_list_1.pop()
print(f'Pop: {test_list_1}')
print(f'Sum list: {test_list_1 + test_list_2}')
print(f'Len: {len(test_list_1)}')
