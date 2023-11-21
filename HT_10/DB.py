import sqlite3


def create_db():
    db = sqlite3.connect('bank.db')
    cursor = db.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
            users_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            UNIQUE(username)

        )
    ''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                balance REAL DEFAULT 0,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        ''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                action TEXT,
                amount REAL,
                timestamp TEXT,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
    ''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS bank_account (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                total_balance REAL  DEFAULT 0 NOT NULL,
                nominal_10 INTEGER  DEFAULT 0 NOT NULL,
                nominal_20 INTEGER DEFAULT 0 NOT NULL,
                nominal_50 INTEGER  DEFAULT 0 NOT NULL,
                nominal_100 INTEGER  DEFAULT 0 NOT NULL,
                nominal_200 INTEGER  DEFAULT 0 NOT NULL,
                nominal_500 INTEGER  DEFAULT 0 NOT NULL,
                nominal_1000 INTEGER  DEFAULT 0 NOT NULL
            )
    ''')

    db.commit()
    db.close()
