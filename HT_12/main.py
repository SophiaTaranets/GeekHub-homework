from User import User
from Validation import Validation, ValidationException
from Bank import Bank
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


def handle_top_up_balance(user: User):
    try:
        v = Validation.Validation
        amount = v.validate_amount(input('Enter income: '))
        amount = user.available_nominal(amount)
        return f'{user.top_up_balance(amount[0])}Change: {amount[1]}\n'
    except Validation.ValidationException as error:
        return error


def handle_take_money_out(user: User):
    try:
        v = Validation.Validation
        amount = v.validate_amount(input('Enter suma you want to get: '))
        amount = user.available_nominal(amount)
        return f'Available nominal: (10, 20, 50, 100, 200, 500, 1000)\n' \
               f'{user.take_money_out(amount[0])}\n'
    except ValidationException as error:
        return error


def handle_change_nominal(bank: Bank):
    try:
        change_nominal_menu()
        v = Validation.Validation
        query = input('Enter your choice: ')
        nominal = v.validate_nominal(input('Enter nominal: '))
        if query == '1':
            new_count = v.validate_amount(input('Enter new count of nominal you want to add to the bank: '))
            bank.add_bank_nominal(nominal, new_count)
            bank.update_bank_balance()
        elif query == '2':
            new_count = v.validate_amount(input('Enter new count of nominal you want to subtract: : '))
            bank.subtract_bank_nominal(nominal, new_count)
            bank.update_bank_balance()
        else:
            return f'Incorrect choice'

        return f'Nominal {nominal} was updated\n' \
               f'Current nominal: {bank.check_bank_nominal()}\n' \
               f'Current bank balance: {bank.check_bank_balance()}\n'
    except Validation.ValidationException as e:
        return e
    finally:
        del bank


def start():
    try:
        name = input('Enter your username: ')
        password = input('Enter your password: ')
        user = User(name, password)
    except KeyError as error:
        print(error)
    else:
        try:
            if user.admin_rules():
                admin()
            elif user.login():
                print('Log in successfully!\n')
                while True:
                    user_menu()
                    query = input('Enter your choice: ')
                    if query == '1':
                        print(f'Current balance: {user.check_user_balance()}\n')

                    elif query == '2':
                        print(handle_top_up_balance(user))

                    elif query == '3':
                        print(handle_take_money_out(user))

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
        bank = Bank()
        while True:
            admin_menu()
            query = input('Enter your choice: ')
            if query == '1':
                print(f'Current bank balance: {bank.check_bank_balance()}\n')

            elif query == '2':
                print(f'Current bank nominal: {bank.check_bank_nominal()}\n')

            elif query == '3':
                print(handle_change_nominal(bank))

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
            v = Validation.Validation
            new_user_name = v.validate_username(input('Enter username: '))
            new_user_password = v.validate_password(input('Enter password: '))
            new_user = User(new_user_name, new_user_password)

            authorization_result = new_user.create_new_user(new_user_name, new_user_password)

            if authorization_result:
                print(f'User \'{new_user_name}\' was successfully created!\n')
                print('Top up your balance now to have chance to get 10% bonus from your balance\n')
                print('Log in:')
                start()
                new_user.get_bonus()
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
