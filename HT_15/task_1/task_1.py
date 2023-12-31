# Викорисовуючи requests, написати скрипт, який буде приймати на вхід ID категорії із сайту
#  https://www.sears.com і буде збирати всі товари із цієї категорії,
# збирати по ним всі можливі дані (бренд, категорія, модель, ціна, рейтинг тощо)
# і зберігати їх у CSV файл (наприклад, якщо категорія має ID 12345,
# то файл буде називатись 12345_products.csv)

# Підказка - відкрийте якусь категорію і досліджуйте запроси,
# які робить браузер, коли ви по ній щось робите - наприклад, переходите на наступну сторінку.
# Підказка 2 - не забувайте використовувати хедери

from sears_api import SearsCategoryAPI

if __name__ == '__main__':
    category_1 = SearsCategoryAPI('1237483576')
    category_1.write_to_file()

    category_2 = SearsCategoryAPI('1320301405')
    category_2.write_to_file()
