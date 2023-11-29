import sqlite3


class Book:
    def __init__(self, title: str = '', author='', year: int = 1600, category_title=''):
        self.title = title
        self.author = author
        self.year = year
        self.category_title = category_title

    @staticmethod
    def input_book_info(self):
        new_title = input('Enter title: ')
        new_author = input('Enter author: ')
        book_year = int(input('Enter year: '))
        category_title = input('Enter title of category: ')

        return(
            new_title,
            new_author,
            book_year,
            category_title)

    @staticmethod
    def __get_category_id(self, title):
        db = sqlite3.connect('library.db')
        cursor = db.cursor()

        cursor.execute('SELECT category_id FROM category WHERE title = ?', (title,))
        result = cursor.fetchone()

        db.close()

        if result:
            return result[0]
        else:
            return None

    def create_new_book(self):
        category_id = self.__get_category_id(self.category_title)
        db = sqlite3.connect('library.db')
        cursor = db.cursor()

        if category_id is not None:
            cursor.execute('''
                INSERT INTO book (title, author_id, year, category_id)
                VALUES (?, ?, ?, ?)
            ''', (self.title, self.author, self.year, category_id))

            db.commit()
            return True
        else:
            db.close()
            return False
