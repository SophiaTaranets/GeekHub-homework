# Create 'list'-like object, but index starts from 1 and index of 0 raises error.
# Тобто це повинен бути клас, який буде поводити себе так,
# як list (маючи основні методи), але індексація повинна починатись із 1

class MyList(list):

    def __getitem__(self, index):
        if isinstance(index, int):
            if index == 0:
                raise IndexError("Index start from 1")
            if index > 0:
                ind = index - 1
            else:
                ind = index
            return list.__getitem__(self, ind)

        elif isinstance(index, slice):
            start, end, step = index.start, index.stop, index.step

            if start is None:
                start = 1

            if end is None:
                end = len(self)

            if step is None:
                step = 1

            if start > 0:
                start -= 1

            if end > 0:
                end -= 1

            return list.__getitem__(self, slice(start, end, step))


# Test list
test_list_1 = MyList(['item 1', 'item 2', 'item 3'])
test_list_2 = MyList(['item 1', 'item 2', 'item 3'])
try:
    print(test_list_1[0])
except IndexError as error:
    print(error)

print(f'First element: {test_list_1[1]}')
print(f'Last element: {test_list_1[-1]}')
print(f'Slice: {test_list_1[1:4]}')
test_list_1.append(100)
test_list_1.extend([200, 300])
print(f'Append-Extend: {test_list_1}')
print(f'Last element: {test_list_1[-1]}')
test_list_1.pop()
print(f'Pop: {test_list_1}')
print(f'Sum list: {test_list_1 + test_list_2}')
print(f'Len: {len(test_list_1)}')
