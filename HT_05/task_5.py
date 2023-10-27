# Ну і традиційно - калькулятор 🙂 Повинна бути 1 ф-цiя, яка б приймала 3 аргументи - один з яких операцiя, яку зробити!
# Аргументи брати від юзера (можна по одному - 2, окремо +, окремо 2; можна всі разом - типу 1 + 2).
# Операції що мають бути присутні: +, -, *, /, %, //, **. Не забудьте протестувати з різними значеннями на предмет помилок!

def calculator(first_number: float, second_number: float, operation: str):
    if operation in ['+', '-', '*', '/', '%', '//', '**']:
        if operation == '+':
            return first_number + second_number
        elif operation == '-':
            return first_number - second_number
        elif operation == '*':
            return first_number * second_number
        elif operation == '/':
            if second_number == 0:
                return 'Error: Division by zero is not allowed.'
            else:
                return first_number / second_number
        elif operation == '%':
            return first_number % second_number
        elif operation == '//':
            if second_number == 0:
                return 'Error: Division by zero is not allowed.'
            else:
                return int(first_number // second_number)
        elif operation == '**':
            return first_number ** second_number
    else:
        return f'Invalid operation. Supported operators are +, -, *, /, %, //, **.'


try:
    x = float(input('Enter first number: '))
    y = float(input('Enter second number: '))
    operator = input('Enter operation: ')
except ValueError as error:
    print(error)
else:
    print(f'Result: {calculator(x, y, operator)}')
