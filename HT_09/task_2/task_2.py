# Написати функцію, яка приймає два параметри: ім'я (шлях) файлу та кількість символів.
# Файл також додайте в репозиторій. На екран повинен вивестись список
# із трьома блоками - символи з початку, із середини та з кінця файлу.
# Кількість символів в блоках - та, яка введена в другому параметрі.
# Придумайте самі, як обробляти помилку, наприклад, коли кількість символів більша,
# ніж є в файлі або, наприклад, файл із двох символів і треба вивести по одному символу,
# то що виводити на місці середнього блоку символів?). Не забудьте додати перевірку чи файл існує.

def check_block_size(file_len, symbols_number):
    if symbols_number > file_len:
        return False
    return True


def file_blocks(file_path, symbols_number: int):
    try:
        with open(file_path, encoding='utf-8') as file:
            content = file.read()

            if not check_block_size(len(content), symbols_number):
                raise ValueError('File consists less symbols than number of symbols')

            start_block = content[:symbols_number]
            end_block = content[-symbols_number:]
            middle_block_start = len(content) // 2 - symbols_number // 2
            middle_block = content[middle_block_start: middle_block_start + symbols_number]

            return f'{start_block}\t{middle_block}\t{end_block}'

    except FileNotFoundError:
        return 'File does not exist'
    except ValueError as e:
        return e


test_file_1 = 'test_1.txt'
test_file_2 = 'test_2.txt'
test_file_3 = 'test_3.txt'
block_size = 3
try:
    print(f'Test 1 (1111222333):\n{file_blocks(test_file_1, block_size)}\n')
    print(f'Test 2 (111222333):\n{file_blocks(test_file_2, block_size)}\n')
    print(f'Test 3 (111):\n{file_blocks(test_file_3, block_size)}\n')
except ValueError as error:
    print(error)
