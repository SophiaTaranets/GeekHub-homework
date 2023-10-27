# Створiть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна повертати якийсь результат
# (напр. інпут від юзера, результат математичної операції тощо).
# Також створiть четверту ф-цiю, яка всередині викликає 3 попереднi,
# обробляє їх результат та також повертає результат своєї роботи.
# Таким чином ми будемо викликати одну (четверту) функцiю, а вона в своєму тiлi - ще 3.
import datetime
from datetime import date


def get_name():
    user_name = input('Enter your name: ')
    return user_name


def calculate_age():
    birth_year = int(input('Enter your birth year: '))
    user_age = datetime.datetime.now().year - birth_year
    return user_age


def check_adult(age: int):
    if age >= 18 and age < 120:
        return True
    else:
        return False


def get_full_info():
    user_name = get_name()
    try:
        user_age = calculate_age()
        if user_age < 0 or user_age >= 120:
            return 'Invalid data: year must be positive, not over then current year and real.'
    except ValueError as error:
        return error
    else:
        is_adult = check_adult(user_age)
        if is_adult:
            return f'Name: {user_name}\nAge: {user_age}\nWelcome to the system!'
        else:
            return f'Name: {user_name}\nAge: {user_age}\nAsk someone of adult to help you.'


print(get_full_info())
