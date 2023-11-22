# Створити клас Person, в якому буде присутнім метод init який буде приймати якісь аргументи,
# які зберігатиме в відповідні змінні.
# - Методи, які повинні бути в класі Person - show_age, print_name, show_all_information.
# - Створіть 2 екземпляри класу Person та в кожному з екземплярів створіть атребут profession
# (його не має інсувати під час ініціалізації).

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def show_age(self):
        print(f'Age: {self.age}')

    def print_name(self):
        print(f'Name: {self.name}')

    def show_all_information(self):
        for field, value in self.__dict__.items():
            print(f'{field}: {value}')


# First instance
person_1 = Person('Monika', 30)

# add profession
person_1.profession = 'Cooker'
person_1.show_all_information()

print('-' * 15)

# Second instance
person_2 = Person('Chandler', 35)

# add profession
person_2.profession = 'Economist'
person_2.show_all_information()
