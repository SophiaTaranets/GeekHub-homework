import User
import Bank
import Validation
from DB import create_db


def authorization_menu():
    print('1 - sign in\n'
          '2 - log in\n'
          f'{"-" * 15}')


def user_menu():
    print('1 - Check balance\n'
          '2 - Top up the balance\n'
          '3 - Take money out\n'
          '0 - Exit\n')


def admin_menu():
    print('1 - Check bank balance\n'
          '2 - Check bank nominal\n'
          '3 - Change nominal\n'
          '0 - Exit\n')


def change_nominal_menu():
    print('1 - add new number of nominal\n'
          '2 - subtract new number of nominal\n')


def handle_top_up_balance(user_id):
    try:
        amount = Validation.validate_amount(input('Enter income: '))
        amount = User.available_nominal(amount)
        return f'{User.top_up_balance(user_id, amount[0])}Change: {amount[1]}\n'
    except Validation.ValidationException as error:
        return error


def handle_take_money_out(users_id):
    try:
        amount = Validation.validate_amount(input('Enter suma you want to get: '))
        return f'{User.take_money_out(users_id, amount)}\n' \
               # f'Change: {}'
    except Validation.ValidationException as error:
        return error


def handle_change_nominal():
    try:
        change_nominal_menu()
        query = input('Enter your choice: ')
        nominal = Validation.validate_nominal(input('Enter nominal: '))
        if query == '1':
            new_count = Validation.validate_amount(input('Enter new count of nominal you want to add to the bank: '))
            Bank.add_bank_nominal(nominal, new_count)
            Bank.update_bank_balance()
        elif query == '2':
            new_count = Validation.validate_amount(input('Enter new count of nominal you want to subtract: : '))
            Bank.subtract_bank_nominal(nominal, new_count)
            Bank.update_bank_balance()
        else:
            return f'Incorrect choice'

        return f'Nominal {nominal} was updated\n' \
               f'Current nominal: {Bank.check_bank_nominal()}\n' \
               f'Current bank balance: {Bank.check_bank_balance()}\n'
    except Validation.ValidationException as e:
        return e


def start():
    try:
        name = input('Enter your username: ')
        password = input('Enter your password: ')
        user_id = User.login(name, password)
    except KeyError as error:
        print(error)
    else:
        try:
            if User.admin_rules(name):
                admin()
            elif user_id is not False:
                print('Log in successfully!\n')
                while True:
                    user_menu()
                    query = input('Enter your choice: ')
                    if query == '1':
                        print(f'Current balance: {User.check_user_balance(user_id)}\n')

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
                print(f'Current bank balance: {Bank.check_bank_balance()}\n')

            elif query == '2':
                print(f'Current bank nominal: {Bank.check_bank_nominal()}\n')

            elif query == '3':
                print(handle_change_nominal())

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

    if authorization_option == '1':

        try:
            new_user_name = Validation.validate_username(input('Enter username: '))
            new_user_password = Validation.validate_password(input('Enter password: '))

            authorization_result = User.create_new_user(new_user_name, new_user_password)

            if authorization_result:
                print(f'User \'{new_user_name}\' was successfully created!\n')
                print('Log in:')
                start()
            else:
                print(f'User is already exist in the system')
                print('Log in:')
                start()
        except Validation.ValidationException as error:
            print(error)

    elif authorization_option == '2':
        start()
    else:
        print('Invalid option')


# create_db()
authorization()
