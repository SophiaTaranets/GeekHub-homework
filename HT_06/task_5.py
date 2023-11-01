# Написати функцію <fibonacci>, яка приймає один аргумент і виводить всі числа Фібоначчі, що не перевищують його.

def fibonacci(number):
    fibonacci_list = []
    a, b = 0, 1
    while a <= number:
        fibonacci_list.append(a)
        a, b = b, a + b
    return fibonacci_list


test_number = 30
print(f'Fibonacci list: {fibonacci(test_number)}')