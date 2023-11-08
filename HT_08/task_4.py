# Реалізуйте генератор, який приймає на вхід будь-яку ітерабельну послідовність (рядок, список, кортеж)
# і повертає генератор, який буде вертати значення з цієї послідовності, при цьому,
# якщо було повернено останній елемент із послідовності - ітерація починається знову.
#    Приклад (якщо запустили його у себе - натисніть Ctrl+C ;) ):
#    for elem in generator([1, 2, 3]):
#        print(elem)
#    1
#    2
#    3
#    1
#    2
#    3
#    1

def generator(elements: [str, list, tuple]):
    if not isinstance(elements, (str, list, tuple)):
        raise ValueError("The input iterable is empty")

    current_index = 0
    while True:
        if current_index < len(elements):
            yield elements[current_index]
            current_index += 1
        else:
            current_index = 0


try:
    for elem in generator([1, 2, 3]):
        print(elem)
except ValueError as error:
    print(error)
