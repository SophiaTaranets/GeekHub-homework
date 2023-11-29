from Book import Book
from Validation import UserException
import sqlite3


class LibraryUser:
    def __init__(self, username: str = "", password: str = "", age: int = 0, phone_number: str = "",
                 status: str = ''):
        self.username = username
        self.password = password
        self.age = age
        self.phone_number = phone_number
        self.status = status

    def _get_user_credentials(self, user_type: str):
        try:
            conn = sqlite3.connect('library.db')
            cursor = conn.cursor()
            cursor.execute(f'SELECT * FROM {user_type}s WHERE username=? AND password=?',
                           (self.username, self.password))
            user = cursor.fetchone()
            cursor.close()
        except sqlite3.Error as e:
            return str(e)
        else:
            return user

    def create_new_user(self, user_type: str):
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        try:
            cursor.execute(f'INSERT INTO {user_type}s (username, password, age, phone_number) '
                           f'VALUES (?, ?, ?, ?)',
                           (self.username, self.password, self.age, self.phone_number))
            conn.commit()

            cursor.execute(f'SELECT user_id FROM {user_type}s WHERE username = ? AND password = ?',
                           (self.username, self.password,))
            id_new_user = cursor.fetchone()[0]

        except sqlite3.IntegrityError:
            conn.close()
            return False
        except sqlite3.Error as e:
            conn.close()
            return str(e)
        finally:
            conn.close()
        return True


class Admin(LibraryUser):
    def __init__(self, username: str = '', password: str = '', age: int = 0, phone_number: str = '',
                 status: str = 'worker'):
        super().__init__(username, password, age, phone_number, status)

    def create_new_user(self, user_type='worker'):
        return super().create_new_user(user_type)

    def login(self):
        self.status = 'worker'
        user = self._get_user_credentials('worker')
        if user:
            return True
        raise UserException('Invalid username or password')

    @staticmethod
    def add_book(new_book: Book):
        new_book.create_new_book()


class Student(LibraryUser):
    def __init__(self, username: str = '', password: str = '', age: int = 0, phone_number: str = '',
                 status: str = 'student',
                 ticket_number: str = ''):

        super().__init__(username, password, age, phone_number, status)
        self.ticket_number = ticket_number

    def create_new_user(self, user_type='student'):
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        try:
            cursor.execute(f'INSERT INTO {user_type}s (username, password, age, phone_number, ticket_number) '
                           f'VALUES (?, ?, ?, ?, ?)',
                           (self.username, self.password, self.age, self.phone_number, self.ticket_number))
            conn.commit()

            cursor.execute(f'SELECT user_id FROM {user_type}s WHERE username = ? AND password = ?',
                           (self.username, self.password,))
            id_new_user = cursor.fetchone()[0]

        except sqlite3.IntegrityError:
            conn.close()
            return False
        except sqlite3.Error as e:
            conn.close()
            return str(e)
        finally:
            conn.close()
        return True

    def login(self):
        self.status = 'student'
        user = self._get_user_credentials('student')
        if user:
            return True
        raise UserException('Invalid username or password')


class Author:
    def __init__(self, id, name):
        self.name = name
        self.id = id
