from User import *
from Bank import *
from Validation import *


def authorization_menu():
    print('Type:\n'
          '\'log in\' if you are in the system\n'
          '\'sign in\' if you are new user\n'
          f'{"-" * 30}')


def user_menu():
    print('1 - Check balance\n'
          '2 - Top up the balance\n'
          '3 - Take money out\n'
          '0 - Exit\n')


def admin_menu():
    print('1 - Check bank balance\n'
          '2 - Check bank nominal\n'
          '3 - Change bank balance\n'
          '4 - Change nominal\n'
          '5 - Exit\n')


def handle_top_up_balance(user_id):
    try:
        amount = validate_amount(input('Enter income: '))
        amount = available_nominal(amount)
        return f'{top_up_balance(user_id, amount[0])}Change: {amount[1]}\n'
    except ValidationException as error:
        return error


def handle_take_money_out(users_id):
    try:
        amount = validate_amount(input('Enter suma you want to get: '))
        return {take_money_out(users_id, amount)}
    except ValidationException as error:
        return error


def handle_top_up_bank_balance():
    try:
        amount = validate_amount(input('Enter suma: '))
        return top_up_bank_balance(amount)
    except ValidationException as e:
        return e


def handle_top_up_bank_nominal():
    try:
        nominal = validate_nominal(input('Enter nominal: '))
        new_count = validate_amount(input('Enter new count of nominal: '))
        return change_bank_nominal(nominal, new_count)
    except ValidationException as e:
        return e


def start():
    try:
        name = input('Enter your username: ')
        password = input('Enter your password: ')
        user_id = login(name, password)
    except KeyError as error:
        print(error)
    else:
        try:
            if admin_rules(name):
                admin()
            if user_id is not False:
                print('Log in successfully!\n')
                while True:
                    user_menu()
                    query = input('Enter your choice: ')
                    if query == '1':
                        print(f'Current balance: {check_user_balance(user_id)}\n')

                    elif query == '2':
                        print(handle_top_up_balance(user_id))

                    elif query == '3':
                        print(handle_take_money_out(user_id))

                    elif query == '0':
                        print("Do you want to exit?")
                        a = input("If yes, type 'yes': ")
                        if a.lower() == "yes":
                            break
                        else:
                            continue
                    else:
                        print('Incorrect choice. Try again.')

        except KeyError as error:
            print(error)


def admin():
    try:
        while True:
            admin_menu()
            query = input('Enter your choice: ')
            if query == '1':
                print(f'Current bank balance: {check_bank_balance()}\n')

            elif query == '2':
                print(f'Current bank nominal: {check_bank_nominal()}\n')

            elif query == '3':
                print(handle_top_up_bank_balance())

            elif query == '4':
                print(handle_top_up_bank_nominal())

            elif query == '0':
                print("Do you want to exit?")
                a = input("If yes, type 'yes': ")
                if a.lower() == "yes":
                    break
                else:
                    continue
            else:
                print('Incorrect choice. Try again.')

    except KeyError as error:
        print(error)


def authorization():
    authorization_menu()
    authorization_option = input('Enter your option: ')

    if authorization_option == 'sign in':

        new_user_name = input('Enter username: ')
        new_user_password = input('Enter password: ')

        try:
            new_user_name = validate_username(new_user_name)
            new_user_password = validate_password(new_user_password)
        except ValidationException as error:
            print(error)

        authorization_result = create_new_user(new_user_name, new_user_password)

        if authorization_result:
            print(f'User \'{new_user_name}\' was successfully created!\n')
            print('Log in:')
            start()
        else:
            print(f'User is already exist in the system')
            print('Log in:')
            start()

    elif authorization_option == 'log in':
        start()
    else:
        print('Invalid option')


# create_db()
authorization()
