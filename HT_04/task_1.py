# Написати скрипт, який приймає від користувача два числа (int або float) і робить наступне:
# a. Кожне введене значення спочатку пробує перевести в int. У разі помилки - пробує перевести в float,
#    а якщо і там ловить помилку - пропонує ввести значення ще раз (зручніше на даному етапі навчання для цього використати цикл while)
# b. Виводить результат ділення першого на друге. Якщо при цьому виникає помилка - оброблює її і виводить відповідне повідомлення

while True:
    first_number = input('Enter the first number: ')
    second_number = input('Enter the second number: ')
    try:
        first_number = int(first_number)
        second_number = int(second_number)
        result = int(first_number) / int(second_number)
    except ValueError:
        try:
            first_number = float(first_number)
            second_number = float(second_number)
            result = float(first_number) / float(second_number)
        except ValueError:
            print('Entered values are false(should be int or float). Try again')
        except ZeroDivisionError as error:
            print(error)
        else:
            print(f'Result: {result}')
            break
    except ZeroDivisionError as error:
        print(error)
    else:
        print(f'Result: {result}')
        break
