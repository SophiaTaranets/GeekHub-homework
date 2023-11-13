# Програма-світлофор.
#    Створити програму-емулятор світлофора для авто і пішоходів.
#    Після запуска програми на екран виводиться в лівій половині - колір автомобільного,
#    а в правій - пішохідного світлофора. Кожну 1 секунду виводиться поточні кольори.
#    Через декілька ітерацій - відбувається зміна кольорів - логіка така сама як і
#    в звичайних світлофорах (пішоходам зелений тільки коли автомобілям червоний).
#    Приблизний результат роботи наступний:
#       Red        Green
#       Red        Green
#       Red        Green
#       Red        Green
#       Yellow     Red
#       Yellow     Red
#       Green      Red
#       Green      Red
#       Green      Red
#       Green      Red
#       Yellow     Red
#       Yellow     Red
#       Red        Green
import time


def traffic_light_emulator(iteration_number: int):
    transport_colors = ['Red', 'Yellow', 'Green']
    pedestrian_colors = ['Green', 'Red']

    transport_index = 0
    pedestrian_index = 0

    time_counter = 0
    for _ in range(iteration_number):
        print(f'{transport_colors[transport_index]}     {pedestrian_colors[pedestrian_index]}')
        time_counter += 1
        time.sleep(1)

        if transport_index == 0 and time_counter == 4:
            transport_index = 1
            pedestrian_index = 1
            time_counter = 0

        elif transport_index == 1 and time_counter == 2:
            transport_index = 2
            pedestrian_index = 1
            time_counter = 0

        elif transport_index == 2 and time_counter == 4:
            transport_index = 0
            pedestrian_index = 0
            time_counter = 0


print('Result')
print('-' * 15)
traffic_light_emulator(20)
