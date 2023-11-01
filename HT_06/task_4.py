# Написати функцію <prime_list>, яка прийматиме 2 аргументи - початок і кінець діапазона,
# і вертатиме список простих чисел всередині цього діапазона. Не забудьте про перевірку на валідність
# введених даних та у випадку невідповідності - виведіть повідомлення.

def is_prime(number: int) -> bool:
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True
    return False


def prime_list(start, end):
    result = []
    for i in range(start, end + 1):
        if is_prime(i):
            result.append(i)
    return result


try:
    start_value = int(input('Enter start value of the range: '))
    end_value = int(input('Enter end value of the range: '))
except ValueError as error:
    print(error)
else:
    print(f'List of prime numbers in range({start_value},{end_value}): {prime_list(start_value, end_value)}')
