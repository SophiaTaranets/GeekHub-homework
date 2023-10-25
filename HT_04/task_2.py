# Create a custom exception class called NegativeValueError.
# Write a Python program that takes an integer as input and raises the NegativeValueError if the input is negative.
# Handle this custom exception with a try/except block and display an error message.

class NegativeValueError(Exception):
    pass


number = int(input('Enter number: '))
try:
    if number < 0:
        raise NegativeValueError('Negative value is not allowed')
except NegativeValueError as error:
    print(error)
