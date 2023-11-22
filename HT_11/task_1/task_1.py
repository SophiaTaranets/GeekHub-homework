# Створити клас Calc, який буде мати атребут last_result та 4 методи.
# Методи повинні виконувати математичні операції з 2-ма числами, а саме додавання, віднімання, множення, ділення.
# - Якщо під час створення екземпляру класу звернутися до атребута last_result він повинен повернути пусте значення.
# - Якщо використати один з методів - last_result повенен повернути результат виконання ПОПЕРЕДНЬОГО методу.
#     Example:
#
#     last_result --> None
#     1 + 1
#     last_result --> None
#     2 * 3
#     last_result --> 2
#     3 * 4
#     last_result --> 6
#     ...

class Calc:

    previous_value = None

    def __init__(self, last_result=None):
        self.last_result = last_result

    def __str__(self):
        return f"{self.last_result}"

    def add(self, first_number: (int, float), second_number: (int, float)):
        result = first_number + second_number
        self.last_result = self.previous_value
        self.previous_value = result
        return result

    def subtraction(self, first_number: (int, float), second_number: (int, float)):
        result = first_number - second_number
        self.last_result = self.previous_value
        self.previous_value = result
        return result

    def multiplication(self, first_number: (int, float), second_number: (int, float)):
        result = first_number * second_number
        self.last_result = self.previous_value
        self.previous_value = result
        return result

    def division(self, first_number: (int, float), second_number: (int, float)):
        try:
            result = first_number / second_number
            self.last_result = self.previous_value
            self.previous_value = result
            return result
        except ZeroDivisionError as error:
            return error


# Test
obj = Calc()
print(obj.last_result)

obj.add(1, 1)
# print(f'Result of adding numbers: {obj.add(1, 1)}')
print(obj.last_result)

obj.multiplication(2, 3)
print(obj.last_result)

obj.multiplication(3, 4)
print(obj.last_result)

obj.multiplication(7, 4)
print(obj.last_result)
