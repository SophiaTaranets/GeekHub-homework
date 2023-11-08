# Напишіть функцію,яка приймає на вхід рядок та повертає кількість окремих регістро-незалежних
# букв та цифр, які зустрічаються в рядку більше ніж 1 раз.
# Рядок буде складатися лише з цифр та букв (великих і малих).
# Реалізуйте обчислення за допомогою генератора.
#
#     Example (input string -> result):
#     "abcde" -> 0            # немає символів, що повторюються
#     "aabbcde" -> 2          # 'a' та 'b'
#     "aabBcde" -> 2          # 'a' присутнє двічі і 'b' двічі (`b` та `B`)
#     "indivisibility" -> 1   # 'i' присутнє 6 разів
#     "Indivisibilities" -> 2 # 'i' присутнє 7 разів та 's' двічі
#     "aA11" -> 2             # 'a' і '1'
#     "ABBA" -> 2             # 'A' і 'B' кожна двічі

def counter(input_string: str):
    input_string = input_string.lower()
    char_numbers = {char: input_string.count(char) for char in set(input_string) if char.isalnum()}
    repeated_count = sum(1 for count in char_numbers.values() if count > 1)

    return repeated_count


# test_string = 'aabbcde'
test_string = 'indivisibility'
try:
    result = counter(test_string)
except ValueError as error:
    print(error)
else:
    print(f'Result: {result}')
