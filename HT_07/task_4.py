# Створіть функцію <morse_code>, яка приймає на вхід рядок у вигляді коду Морзе та
# виводить декодоване значення (латинськими літерами).
#    Особливості:
#     - використовуються лише крапки, тире і пробіли (.- )
#     - один пробіл означає нову літеру
#     - три пробіли означають нове слово
#     - результат може бути case-insensetive (на ваш розсуд - велики чи маленькими літерами).
#     - для простоти реалізації - цифри, знаки пунктуацїї, дужки, лапки тощо використовуватися не будуть. Лише латинські літери.
#     - додайте можливість декодування сервісного сигналу SOS (...---...)

#     Приклад:
#     --. . . -.- .... ..- -...   .. ...   .... . .-. .
#     результат: GEEKHUB IS HERE

class MorseException(Exception):
    pass


def morse_code(morse_string: str) -> str:
    morse_code_dictionary = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
        '--..': 'Z', ' ': ' ', '...---...': 'SOS'
    }
    pattern = ['.', '-', ' ']
    if any([symbol for symbol in morse_string if symbol not in pattern]):
        raise MorseException('Morse code must consist only (. -) symbols')

    decode_words = []
    words = morse_string.split('   ')

    for word in words:
        decode_word = []
        letters = word.split(' ')

        for letter in letters:
            for morse_symbol, latin_letter in morse_code_dictionary.items():
                if letter == morse_symbol:
                    decode_word.append(latin_letter)
        decode_words.append(''.join(decode_word))
    decode_morse_string = ' '.join(decode_words)

    return decode_morse_string


morse_message = '--. . . -.- .... ..- -...   .. ...   .... . .-. .'
# sos_message = '...---...'
try:
    decode_morse_message = morse_code(morse_message)
except MorseException as error:
    print(error)
else:
    print(f'Decode message: {decode_morse_message}')
