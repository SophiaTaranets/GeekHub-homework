# Написати функцію, яка приймає на вхід список (через кому), підраховує кількість однакових елементів у ньомy і виводить результат.
# Елементами списку можуть бути дані будь-яких типів.
#     Наприклад:
#     1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2] ----> "1 -> 3, foo -> 2, [1, 2] -> 2, True -> 1"

def similar_elements(lst: list):
    count_elements = {}
    for element in lst:
        if isinstance(element, (bool, type(None))):
            k = element
        else:
            k = str(element)
        if k in count_elements:
            count_elements[k] += 1
        else:
            count_elements[k] = 1
    result = []
    for key, value in count_elements.items():
        result.append(f'{key} -> {value}')
    return ', '.join(result)


test_list = [1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2], 'True', None, 'None', (1, 2), {1: 1, 2: 4}, {1, 2}, {1, 2}]
print(f'Result: {similar_elements(test_list)}')
