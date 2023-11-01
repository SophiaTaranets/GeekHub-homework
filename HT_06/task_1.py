# Написати функцію <square>, яка прийматиме один аргумент - сторону квадрата,
# і вертатиме 3 значення у вигляді кортежа: периметр квадрата, площа квадрата та його діагональ.
import math


def square(side_square: float):
    perimetr = 4 * side_square
    area = side_square * side_square
    diagonal = math.sqrt(side_square ** 2 + side_square ** 2)
    result = (perimetr, area, round(diagonal,3))
    return result


try:
    side = float(input('Enter side of square: '))
except ValueError as error:
    print(error)
else:
    print(square(2))
