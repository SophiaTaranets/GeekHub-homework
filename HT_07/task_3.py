# На основі попередньої функції (скопіюйте кусок коду) створити наступний скрипт:
#    а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
#    б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором,
#    перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення, наприклад:
#       Name: vasya
#       Password: wasd
#       Status: password must have at least one digit
#       -----
#       Name: vasya
#       Password: vasyapupkin2000
#       Status: OK
#    P.S. Не забудьте використати блок try/except ;)
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

    if not (any([i.isdigit() for i in password])):
        raise ValidationException('Password must consist at least 1 digit symbol')

    return True


users = [
        {'username': 'Tom', 'password': 'qW123!'},
        {'username': 'Olena', 'password': 'qWf78123!'},
        {'username': 'Alex', 'password': 'password'},
        {'username': 'Anna@gmail.com', 'password': 'password4'},
        {'username': 'a', 'password': 'password5'}
]
for user in users:
    try:
        if credentials_validation(user['username'], user['password']):
            print(f"{user['username']}\nPassword: {user['password']}\nStatus: OK\n")
    except ValidationException as error:
        print(f"{user['username']}\nPassword: {user['password']}\nStatus: {error}\n")
