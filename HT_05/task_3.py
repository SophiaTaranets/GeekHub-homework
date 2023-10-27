# Користувач вводить змiннi "x" та "y" з довiльними цифровими значеннями.
# Створiть просту умовну конструкцiю (звiсно вона повинна бути в тiлi ф-цiї),
# пiд час виконання якої буде перевiрятися рiвнiсть змiнних "x" та "y" та у випадку нервіності - виводити ще і різницю.
#     Повиннi опрацювати такi умови (x, y, z заміність на відповідні числа):
#     x > y;       вiдповiдь - "х бiльше нiж у на z"
#     x < y;       вiдповiдь - "у бiльше нiж х на z"
#     x == y.      вiдповiдь - "х дорiвнює z"


def check_values(a, b):
    if a > b:
        return f'{a} greater than {b} times {a - b}'
    elif a < b:
        return f'{b} greater than {a} times {b - a}'
    else:
        return f'{a} equal {b}'


try:
    x = int(input('Enter x: '))
    y = int(input('Enter y: '))
except ValueError as error:
    print(error)
else:
    print(check_values(x, y))
