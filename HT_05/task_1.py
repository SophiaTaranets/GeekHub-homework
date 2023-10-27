# Написати функцiю season, яка приймає один аргумент (номер мiсяця вiд 1 до 12)
# та яка буде повертати пору року, якiй цей мiсяць належить (зима, весна, лiто або осiнь).
# У випадку некоректного введеного значення - виводити відповідне повідомлення

def season(month_number: int) -> str:
    if month_number in [12, 1, 2]:
        return 'Season: winter'
    elif month_number in [3, 4, 5]:
        return 'Season: spring'
    elif month_number in [6, 7, 8]:
        return 'Season: summer'
    elif month_number in [9, 10, 11]:
        return 'Season: autumn'
    else:
        return 'False data: number of month must be between 1 an 12'


try:
    month = int(input('Enter number of month: '))
    result = season(month)
except ValueError as error:
    print(error)
else:
    print(result)
