# Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
# Тобто щоб її можна було використати у вигляді:
#     for i in my_range(1, 10, 2):
#         print(i)
#     1
#     3
#     5
#     7
#     9

def range_generator(start: int = 0, stop=None, step: int = 1):
    if stop is None:
        start, stop = 0, start
    current_element = start
    if step > 0:
        while current_element < stop:
            yield current_element
            current_element += step
    elif step < 0:
        while current_element > stop:
            yield current_element
            current_element += step
    else:
        raise ValueError('Step can`t equal zero')

try:
    for i in range_generator(1, 10, 2):
        print(i)
except ValueError as error:
    print(error)
