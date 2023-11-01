# Написати функцію, яка буде реалізувати логіку циклічного зсуву елементів в списку.
# Тобто функція приймає два аргументи: список і величину зсуву
# (якщо ця величина додатня - пересуваємо з кінця на початок, якщо від'ємна - навпаки - пересуваємо елементи з початку списку в його кінець).
#    Наприклад:
#    fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1, 2, 3, 4]
#    fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2]

def list_shift(lst: list, shift: int) -> list:
    if not lst:
        return lst

    shift = shift % len(lst)

    if shift == 0:
        return lst

    if shift > 0:
        return lst[-shift:] + lst[:-shift]
    else:
        return lst[-shift:] + lst[:-shift]


test_list_1 = [1, 2, 3, 4, 5]
shift_1 = 1
print(f'Result 1: {list_shift(test_list_1, shift_1)}')

test_list_2 = [1, 2, 3, 4, 5]
shift_2 = -2
print(f'Result 2: {list_shift(test_list_2, shift_2)}')
