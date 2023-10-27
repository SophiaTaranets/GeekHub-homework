# Наприклад маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfe  kdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p4 65jnpoj35po6j345"
# -> просто потицяв по клавi =)
#    Створіть ф-цiю, яка буде отримувати рядки на зразок цього та яка оброблює наступні випадки:
# -  якщо довжина рядка в діапазонi 30-50 (включно) -> прiнтує довжину рядка, кiлькiсть букв та цифр
# -  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр лише з буквами (без пробілів)
# -  якщо довжина більше 50 -> щось вигадайте самі, проявіть фантазію =)

def check_string(value: str):
    value_len = len(value)
    if 30 <= value_len <= 50:
        char_len = len([i for i in value if i.isalpha()])
        digit_len = len([i for i in value if i.isdigit()])
        print(f'Length of string: {value_len}\nNumber of char: {char_len}\nNumber of digits: {digit_len}')
    elif value_len < 30:
        sum_digits = sum([int(i) for i in value if i.isdigit()])
        chars = ''.join([i for i in value if i.isalpha()])
        print(f'Sum of all digits: {sum_digits}\nString without digits: {chars}')
    elif value_len > 50:
        # print only vowels chars
        chars = [i for i in value if i.isalpha()]
        vowels_char = ''.join([i for i in chars if i in ['a', 'o', 'i', 'e', 'y', 'u']])

        # print digits over than 5
        digits_over_five = [int(i) for i in value if i.isdigit() and int(i) > 5]
        digits_over_five = ''.join(list(map(str, digits_over_five)))

        print(f'Vowels chars: {vowels_char}\nDigits over 5: {digits_over_five}')


# string_value = '440505glglglwa iu0'
# string_value = '440505glglglwa ilfldorfvvkfm00332435252223424u0'
string_value = 'f98neroi4nr0c3n30irn03ien3c0rfe  kdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p4 65jnpoj35po6j345'
check_string(string_value)
