# Написати функцію, яка приймає два параметри: ім'я (шлях) файлу та кількість символів.
# Файл також додайте в репозиторій. На екран повинен вивестись список
# із трьома блоками - символи з початку, із середини та з кінця файлу.
# Кількість символів в блоках - та, яка введена в другому параметрі.
# Придумайте самі, як обробляти помилку, наприклад, коли кількість символів більша,
# ніж є в файлі або, наприклад, файл із двох символів і треба вивести по одному символу,
# то що виводити на місці середнього блоку символів?). Не забудьте додати перевірку чи файл існує.

def file_blocks(file_path, symbols_number):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

            if len(content) < symbols_number:
                raise ValueError('File consists less symbols than number of symbols')

            start_block = content[:symbols_number]
            middle_block_start = len(content) // 2 - symbols_number // 2
            middle_block = content[middle_block_start: middle_block_start + symbols_number]
            end_block = content[-symbols_number:]
            return f'{start_block}\n{end_block}\n{middle_block}'

    except FileExistsError:
        return 'File does not exist'
    except ValueError:
        return 'Invalid value'
    except Exception:
        return 'Unexpected error'


file_name = 'information'
block_size = 20
try:
    print(file_blocks(file_name, block_size))
except ValueError as error:
    print(error)
