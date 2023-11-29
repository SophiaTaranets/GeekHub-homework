from LibraryUser import Student, Admin
from Category import Category
from Validation import UserException
from DB import create_db


def enter_menu():
    print('1 - log in\n'
          '2 - sign in\n')


def rules():
    print('1 - student\n'
          '2 - admin\n')


def log_in():
    name = input('Enter name: ')
    password = input('Enter password: ')
    rules()
    option = input('Choose your option: ')
    if option == '1':
        try:
            student = Student(username=name, password=password)
            student.login()
            return student
        except UserException as e:
            return e
    elif option == '2':
        try:
            worker = Admin(username=name, password=password)
            worker.login()
            return worker
        except UserException as e:
            return e


def sign_in():
    name = input('Enter your name: ')
    password = input('Enter your password: ')
    age = int(input('Enter your age: '))
    phone_number = input('Enter your phone number: ')

    print('1 - student\n'
          '2 - admin\n')

    option = input('Enter your option: ')
    status = ''
    if option == '1':
        ticket_number = input('Enter number of the ticket: ')
        student = Student(name, password, age, phone_number, ticket_number)
        status = student.create_new_user()
    elif option == '2':
        admin = Admin(name, password, age, phone_number)
        status = admin.create_new_user()
    if status:
        print('Sign in successfully!')
    else:
        print('Something went wrong')


def worker_menu():
    while True:
        print('1 - create new category\n'
              '2 - check all categories\n'
              '0 - exit\n')
        option = input('Enter option: ')
        c = Category()
        if option == '1':
            category_name = input('Enter name of category: ')
            result = c.create_category(category_name)
            if result:
                print('Category was successfully created!')
        elif option == '2':
            for category in c.get_all_categories():
                print(category[0])
        elif option == '0':
            break
        else:
            print("Invalid option")


def student_menu():
    while True:
        print('1 - check all categories\n'
              '0 - exit\n')
        option = input('Enter option: ')
        c = Category()
        if option == '1':
            for category in c.get_all_categories():
                print(category[0])
        elif option == '0':
            break
        else:
            print("Invalid option")


def main():
    enter_menu()
    query = input('Enter query: ')

    if query == '1':
        try:
            user = log_in()
            if isinstance(user, UserException):
                print(f"Error: {user}")
            else:
                if user.status == 'worker':
                    worker_menu()
                elif user.status == 'student':
                    student_menu()
        except UserException as e:
            print(f"Error: {e}")
    elif query == '2':
        sign_in()
    else:
        print('Incorrect option!')


create_db()
main()
