# Create 'list'-like object, but index starts from 1 and index of 0 raises error.
# Тобто це повинен бути клас, який буде поводити себе так,
# як list (маючи основні методи), але індексація повинна починатись із 1

class MyList:
    def __init__(self):
        self._data = []

    def __getitem__(self, index):
        if index < 1 or index > len(self._data):
            raise IndexError("Index out of range")
        return self._data[index - 1]

    def __setitem__(self, index, value):
        if index < 1 or index > len(self._data):
            raise IndexError("Index out of range")
        self._data[index - 1] = value

    def append(self, value):
        self._data.append(value)

    def extend(self, values):
        self._data.extend(values)

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return repr(self._data)


my_test_list = MyList()
my_test_list.append(20)
my_test_list.append(21)
print(f'Append: {my_test_list}')
my_test_list.extend([100, 200])
print(f'Extended: {my_test_list}')
print(f'Len: {len(my_test_list)}')

try:
    print(my_test_list[1])
    print(my_test_list[3])
    print(my_test_list[0])
    print('-' * 15)
except IndexError as e:
    print(e)
