import sqlite3
from datetime import datetime
from Bank import check_bank_balance, update_bank_balance


def create_new_user(username: str, password: str):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()

        cursor.execute('SELECT users_id FROM users WHERE username = ? AND password = ?', (username, password))
        id_new_user = cursor.fetchone()[0]

        cursor.execute('INSERT INTO accounts (user_id) VALUES (?)', (id_new_user,))
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        return False
    finally:
        conn.close()
    return True


def read_user_credentials(username: str, password: str):
    try:
        conn = sqlite3.connect('bank.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
        user = cursor.fetchone()
        cursor.close()
    except Exception as e:
        return e
    else:
        return user


def login(username: str, password: str):
    user = read_user_credentials(username, password)
    if user:
        return user[0]
    raise KeyError('Invalid username or password')


def check_user_balance(user_id):
    try:
        conn = sqlite3.connect('bank.db')
        cursor = conn.cursor()
        cursor.execute('SELECT balance FROM accounts WHERE user_id=?', (user_id,))
        balance = cursor.fetchone()
        conn.close()
    except Exception as e:
        return e
    else:
        return balance[0]


def available_nominal(amount):
    suma, change = 0, 0
    if amount % 10 == 0:
        amount = amount
    else:
        change = amount % 10
        change = change
    amount = amount - change
    return amount, change


def top_up_balance(user_id, income):
    update_bank_balance()
    try:
        conn = sqlite3.connect('bank.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE accounts SET balance = balance + ? WHERE user_id = ?', (income, user_id, ))
        conn.commit()

        transactions_time = str(datetime.now())
        cursor.execute('INSERT INTO transactions (user_id, action, amount, timestamp) VALUES (?, ?, ?, ?)',
                       (user_id, 'top_up', income, transactions_time, ))
        conn.commit()

        cursor.execute('SELECT balance FROM accounts WHERE user_id = ?', (user_id,))
        balance = cursor.fetchone()
        conn.close()

    except Exception as e:
        return e
    return f'Your balance was replenished with {income} uah\nCurrent balance: {balance[0]}\n'


def take_money_out(user_id, suma):
    update_bank_balance()
    try:
        suma = float(suma)
        conn = sqlite3.connect('bank.db')
        cursor = conn.cursor()
        cursor.execute('SELECT balance FROM accounts WHERE user_id = ?', (user_id,))
        current_balance = cursor.fetchone()[0]

        bank_balance = check_bank_balance()

        if current_balance < suma:
            conn.close()
            return 'You don`t have enough money.\n'

        if suma > bank_balance:
            conn.close()
            return 'Bank does not have enough funds to carry out the transaction\n'

        cursor.execute('UPDATE accounts SET balance = balance - ? WHERE user_id = ?', (suma, user_id,))
        conn.commit()

        transactions_time = str(datetime.now())
        cursor.execute('INSERT INTO transactions (user_id, action, amount, timestamp) VALUES (?, ?, ?, ?)',
                       (user_id, 'money_out', suma, transactions_time,))
        conn.commit()

        cursor.execute('SELECT balance FROM accounts WHERE user_id = ?', (user_id,))
        new_balance = cursor.fetchone()[0]
        conn.close()
    except Exception as e:
        return e
    return f'Your balance was down with {suma} uah\nCurrent balance: {new_balance}\n'


def admin_rules(username):
    if username == 'admin':
        return True
    else:
        return False
