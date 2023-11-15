# Програма-банкомат.
#    Використувуючи функції створити програму з наступним функціоналом:
#       - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль (файл <users.CSV>);
#       - кожен з користувачів має свій поточний баланс (файл <{username}_balance.TXT>)
#       та історію транзакцій (файл <{username_transactions.JSON>);
#       - є можливість як вносити гроші, так і знімати їх.

#       Обов'язкова перевірка введених даних (введено цифри; знімається не більше, ніж є на рахунку і т.д.).
#    Особливості реалізації:
#       - файл з балансом - оновлюється кожен раз при зміні балансу (містить просто цифру з балансом);
#       - файл - транзакціями - кожна транзакція у вигляді JSON рядка додається в кінець файла;
#       - файл з користувачами: тільки читається. Але якщо захочете реалізувати функціонал додавання нового користувача - не стримуйте себе :)
#    Особливості функціонала:
#       - за кожен функціонал відповідає окрема функція;
#       - основна функція - <start()> - буде в собі містити весь workflow банкомата:
#       - на початку роботи - логін користувача (програма запитує ім'я/пароль). Якщо вони неправильні -
#       вивести повідомлення про це і закінчити роботу (хочете - зробіть 3 спроби, а потім вже закінчити роботу - все на ентузіазмі :))
#       - потім - елементарне меню типн:
#         Введіть дію:
#            1. Продивитись баланс
#            2. Поповнити баланс
#            3. Вихід
#       - далі - фантазія і креатив, можете розширювати функціонал, але основне завдання має бути повністю реалізоване :)
#     P.S. Увага! Файли мають бути саме вказаних форматів (csv, txt, json відповідно)
#     P.S.S. Добре продумайте структуру програми та функцій

import csv
import json
from datetime import datetime
import re


# def file_validation(filename):
#     try:
#         with open(filename):
#             return True
#     except FileExistsError:
#         return 'File can not be opened'


class ValidationException(Exception):
    pass


def read_user_credentials(filename):
    try:
        data = {}
        with open(filename, encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for i, row in enumerate(reader):
                data[i] = {'username': row['username'], 'password': row['password']}
        return data
    except FileNotFoundError:
        return {}


def login(username: str, password: str, credentials_dict: dict):
    for value in credentials_dict.values():
        if value['username'] == username and value['password'] == password:
            return True
    raise KeyError('Invalid username or password')


def validate_amount(amount_str):
    try:
        amount = float(amount_str)
        if amount <= 0:
            raise ValidationException('Amount must be a positive number.')
    except ValueError:
        raise ValidationException('Amount must be a valid number.')

    return amount


def check_user_balance(filename):
    try:
        with open(filename, encoding='utf-8') as file:
            balance = file.read()
    except FileNotFoundError:
        return 'Your balance file is missing'
    else:
        return f'Your current balance: {balance}\n' if balance else 'Your balance is empty\n'


def top_up_balance(filename, income):
    try:
        with open(filename, encoding='utf-8') as file:
            current_balance = file.read()
        with open(filename, 'w', encoding='utf-8') as file:
            if current_balance == '':
                new_balance = validate_amount(income)
            else:
                new_balance = float(current_balance) + income
            file.write(str(new_balance))
    except FileNotFoundError:
        return 'Your balance file is missing'
    return f'Your balance was replenished with {income} uah\nCurrent balance: {new_balance}\n'


def take_money_out(filename, suma):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            current_balance = file.read()
        with open(filename, 'w', encoding='utf-8') as file:
            if current_balance == '':
                return 'Your balance is empty.'
            else:
                if float(current_balance) < suma:
                    return 'You don`t have enough money.'
                else:
                    new_balance = float(current_balance) - suma
            file.write(str(new_balance))

    except FileExistsError:
        return 'Your balance file is missing'
    return f'Your balance was down with {suma} uah\nCurrent balance: {new_balance}.'


def log_transactions(filename, action, amount):
    try:
        transactions_time = str(datetime.now())
        transactions = {
            'transactions_time': transactions_time,
            'action': action,
            'amount': amount
        }

        with open(filename, 'a', encoding='utf-8') as file:
            json.dump(transactions, file)
            file.write('\n')
        return 'Transaction logged successfully.'
    except FileNotFoundError:
        return 'Your transaction log file is missing.'


def menu():
    print('1 - Check balance')
    print('2 - Top up the balance')
    print('3 - Take money out')
    print('0 - Exit')


def start():
    try:
        name = input('Enter your username: ')
        password = input('Enter your password: ')
        users_file = 'users.csv'
        users_balance = f'{name}_balance.txt'
        users_transactions = f'{name}_transactions.json'

    except ValidationException as error:
        print(error)

    else:
        try:
            users_data = read_user_credentials(users_file)
            authorisation_result = login(name, password, users_data)
            if authorisation_result is not False:
                print('Log in successfully!\n')
                while True:
                    menu()
                    query = input('Enter your choose: ')
                    if query == '1':
                        print(check_user_balance(users_balance))

                    elif query == '2':
                        try:
                            income = validate_amount(input('Enter income: '))
                            log_transactions(users_transactions, 'top_up', income)
                            print(top_up_balance(users_balance, income))
                        except ValidationException as error:
                            print(error)

                    elif query == '3':
                        try:
                            suma = validate_amount(input('Enter suma you want to get: '))
                            log_transactions(users_transactions, 'money_down', suma)
                            print(take_money_out(users_balance, suma))
                        except ValidationException as error:
                            print(error)
                    elif query == '0':
                        print(f"Do you want to exit?")
                        a = input("If yes, type 'yes': ")
                        if a == "yes":
                            break
                        else:
                            continue
                    else:
                        print('Incorrect chosen. Try again.')

        except KeyError as error:
            print(error)


start()
