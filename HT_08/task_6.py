# Напишіть функцію,яка прймає рядок з декількох слів і повертає довжину найкоротшого слова.
# Реалізуйте обчислення за допомогою генератора.

def short_string(input_string: str):
    words = input_string.split()
    if len(words) == 0:
        return 0
    words_length = (len(word) for word in words)
    min_word_length = min(words_length)
    return min_word_length


test_string = 'The shortest word in string'
try:
    result = short_string(test_string)
except ValueError as error:
    print(error)
else:
    print(f'Len of the shortest word: {result}')
