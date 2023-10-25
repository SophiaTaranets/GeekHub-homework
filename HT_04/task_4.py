# Write a Python program that demonstrates exception chaining.
# Create a custom exception class called CustomError and another called SpecificError.
# In your program (could contain any logic you want), raise a SpecificError,
# and then catch it in a try/except block, re-raise it as a CustomError with the original exception as the cause.
# Display both the custom error message and the original exception message.
from datetime import datetime


class CustomError(Exception):
    pass


class SpecificError(Exception):
    pass


try:
    birth_date = input('Enter your birth date in the format dd-mm-yyyy: ')
    try:
        parsed_date = datetime.strptime(birth_date, '%d-%m-%Y')
    except ValueError as value_error:
        raise SpecificError('Specific Error, Invalid format') from value_error
except SpecificError as specific_error:
    try:
        raise CustomError('Custom Error') from specific_error
    except CustomError as custom_error:
        print(f'Error: {custom_error}')
        print(f'Original exception: {custom_error.__cause__}')
else:
    print(f'Parsed date: {parsed_date}')
