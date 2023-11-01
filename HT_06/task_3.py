# Написати функцию <is_prime>, яка прийматиме 1 аргумент - число від 0 до 1000,
# и яка вертатиме True, якщо це число просте і False - якщо ні.

def is_prime(number: int) -> bool:
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True
    return False


try:
    test_number = int(input('Enter number: '))
    if test_number < 0:
        print('Number should be in range of 1 to 1000')
except ValueError as error:
    print(error)
else:
    print(is_prime(test_number))
