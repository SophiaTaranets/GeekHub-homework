# Create a Python script that takes an age as input.
# If the age is less than 18 or greater than 120, raise a custom exception called InvalidAgeError.
# Handle the InvalidAgeError by displaying an appropriate error message.

class InvalidAgeError(Exception):
    pass


while True:
    try:
        age = int(input('Enter your age: '))
        if age < 18 or age > 120:
            raise InvalidAgeError('Age error. Age should be less than 18 or greater than 120.')
    except ValueError:
        print('Entered value is invalid. Try again')
    except InvalidAgeError as error:
        print(error)
    else:
        print(f'Age: {age}')
        break
