# 1. Напишіть програму, де клас «геометричні фігури» (Figure) містить властивість color з початковим значенням white
# і метод для зміни кольору фігури, а його підкласи «овал» (Oval) і «квадрат» (Square) містять методи init для
# завдання початкових розмірів об'єктів при їх створенні.
import math


class Figure:
    def __init__(self, color: str = 'white'):
        self.color = color

    @staticmethod
    def _color_options():
        print('1 - blue\n'
              '2 - green\n'
              '3 - red\n'
              '4 - pink\n'
              '5 - brown\n')

    def change_color(self):

        print('1 - Choose color from the list\n'
              '2 - Choose one color\n')
        option = input('Enter your option: ')
        if option == '1':
            self._color_options()
            color_option = input('Enter color option: ')
            if color_option == '1':
                self.color = 'blue'
            elif color_option == '2':
                self.color = 'green'
            elif color_option == '3':
                self.color = 'red'
            elif color_option == '4':
                self.color = 'pink'
            elif color_option == '5':
                self.color = 'brown'
        elif option == '2':
            new_color = input('Enter new color: ')
            self.color = new_color
        else:
            print('Incorrect option.')

        return self.color


class Oval(Figure):
    def __init__(self, color='white', small_radius=10, big_radius = 20):
        super().__init__(color)
        self.big_radius = big_radius
        self.small_radius = small_radius

    def area(self):
        return round(self.big_radius * self.small_radius * math.pi, 3)


class Square(Figure):
    def __init__(self, color='white', side=10):
        super().__init__(color)
        self.side = side

    def area(self):
        return self.side ** 2


# instances of classes

test_figure = Figure()
print(f'Color before changes: {test_figure.color}')
print(f'Color after changes: {test_figure.change_color()}')
print(f'Figure color: {test_figure.color}')

test_oval = Oval()
print(f'Area of oval: {test_oval.area()}')

test_square = Square()
print(f'Area of square: {test_square.area()}')