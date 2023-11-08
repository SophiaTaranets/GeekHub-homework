# Запишіть в один рядок генератор списку (числа в діапазоні від 0 до 100), сума цифр кожного елемент якого буде дорівнювати 10.
#    Результат: [19, 28, 37, 46, 55, 64, 73, 82, 91]

def digits_sum(number: int):
    return sum([int(digit) for digit in str(number)])


list_generator = [i for i in range(0, 100) if digits_sum(i) == 10]
print(f'Result: {list_generator}')
