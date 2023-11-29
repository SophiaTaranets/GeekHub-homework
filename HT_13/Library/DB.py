import sqlite3


def create_db():
    db = sqlite3.connect('library.db')
    cursor = db.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS workers (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            age INTEGER NOT NULL,
            phone_number TEXT NOT NULL,
            status TEXT DEFAULT 'admin' NOT NULL,
            UNIQUE(username)
        )
    ''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                age INTEGER NOT NULL,
                phone_number TEXT NOT NULL,
                status TEXT DEFAULT 'student' NOT NULL,
                ticket_number TEXT NOT NULL,
                UNIQUE(username)
            )
        ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS category (
            category_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS author (
            author_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')

    # Таблиця книг
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS book (
            book_id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_id INTEGER,
            title TEXT NOT NULL,
            author_id INTEGER,
            year INTEGER,
            category_title TEXT NOT NULL,
            FOREIGN KEY (author_id) REFERENCES author(author_id)
        )
    ''')

    db.commit()
    db.close()
