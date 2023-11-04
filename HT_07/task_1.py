# Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
# Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>)
# і третій - необов'язковий параметр <silent> (значення за замовчуванням - <False>).
# Логіка наступна:
#     якщо введено коректну пару ім'я/пароль - вертається True;
#     якщо введено неправильну пару ім'я/пароль:
#         якщо silent == True - функція вертає False
#         якщо silent == False -породжується виключення LoginException (його також треба створити =))

class LoginException(Exception):
    pass


def check_user_credentials(username: str, password: str, silent: bool = False) -> bool:
    users = [
        {'username': 'Tom', 'password': 'password1'},
        {'username': 'Olena', 'password': 'password2'},
        {'username': 'Alex', 'password': 'password3'},
        {'username': 'Anna', 'password': 'password4'},
        {'username': 'Oleg', 'password': 'password5'}
    ]

    for user in users:
        if user['username'] == username and user['password'] == password:
            return True
    if silent:
        return False
    else:
        raise LoginException('Incorrect username or password')


user_name = input('Enter username: ')
user_password = input('Enter password: ')
try:
    result = check_user_credentials(user_name, user_password)
    print(result)
except LoginException as error:
    print(error)
