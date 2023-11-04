# Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
#    - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
#    - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну
#    цифру;
#    - якесь власне додаткове правило :)
#    Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.
import re


class ValidationException(Exception):
    pass


def credentials_validation(username: str, password: str):
    special_characters_pattern = re.compile(r'[!@#$%^&*(),.?":{}|<>]')
    if not len(username) in range(3, 51):
        raise ValidationException('User name consist symbols in range in 3 to 50')

    # additional rule: username can`t consist special symbols
    if special_characters_pattern.search(username):
        raise ValidationException('Username can`t consist special symbols')

    if not len(password) >= 8:
        raise ValidationException('Password must consist at least 8 symbols')

    if not (any([symbol.isdigit() for symbol in password])):
        raise ValidationException('Password must consist at least 1 digit symbol')

    return True


user_name = input('Enter username: ')
user_password = input('Enter password: ')
try:
    result = credentials_validation(user_name, user_password)
except ValidationException as error:
    print(error)
else:
    print(result)



