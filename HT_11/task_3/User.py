import random
import sqlite3
from datetime import datetime
from Bank import Bank

class User:
    def __init__(self, username: str, password: str):
        # self.user_id = user_id
        self.username = username
        self.password = password

    def __get_user_id(self):
        user = self.__get_user_credentials(self.username, self.password)
        if user:
            return user[0]

    @staticmethod
    def __get_user_credentials(username: str, password: str):
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

    @staticmethod
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

    def login(self):
        user = self.__get_user_credentials(self.username, self.password)
        if user:
            return True
        raise KeyError('Invalid username or password')

    @staticmethod
    def available_nominal(amount):
        suma, change = 0, 0
        if amount % 10 == 0:
            amount = amount
        else:
            change = amount % 10
            change = change
        amount = amount - change
        return amount, change

    def check_user_balance(self):
        try:
            conn = sqlite3.connect('bank.db')
            cursor = conn.cursor()
            cursor.execute('SELECT balance FROM accounts WHERE user_id=?', (self.__get_user_id(),))
            balance = cursor.fetchone()
            conn.close()
        except Exception as e:
            return e
        else:
            return balance[0]

    def top_up_balance(self, amount):
        # update_bank_balance()
        try:
            conn = sqlite3.connect('bank.db')
            cursor = conn.cursor()
            cursor.execute('UPDATE accounts SET balance = balance + ? WHERE user_id = ?', (amount, self.__get_user_id(),))
            conn.commit()

            transactions_time = str(datetime.now())
            cursor.execute('INSERT INTO transactions (user_id, action, amount, timestamp) VALUES (?, ?, ?, ?)',
                           (self.__get_user_id(), 'top_up', amount, transactions_time,))
            conn.commit()

            cursor.execute('SELECT balance FROM accounts WHERE user_id = ?', (self.__get_user_id(),))
            balance = cursor.fetchone()
            conn.close()

        except Exception as e:
            return e
        return f'Your balance was replenished with {amount} uah\nCurrent balance: {balance[0]}\n'

    def take_money_out(self, amount):
        # update_bank_balance()
        try:
            amount = float(amount)
            conn = sqlite3.connect('bank.db')
            cursor = conn.cursor()
            cursor.execute('SELECT balance FROM accounts WHERE user_id = ?', (self.__get_user_id(),))
            current_balance = cursor.fetchone()[0]

            # bank_balance = check_bank_balance()
            bank_balance = 7700
            if current_balance < amount:
                conn.close()
                return 'You don`t have enough money.\n'

            if amount > bank_balance:
                conn.close()
                return 'Bank does not have enough funds to carry out the transaction\n'

            cursor.execute('UPDATE accounts SET balance = balance - ? WHERE user_id = ?', (amount, self.__get_user_id(),))
            conn.commit()

            transactions_time = str(datetime.now())
            cursor.execute('INSERT INTO transactions (user_id, action, amount, timestamp) VALUES (?, ?, ?, ?)',
                           (self.__get_user_id(), 'money_out', amount, transactions_time,))
            conn.commit()

            cursor.execute('SELECT balance FROM accounts WHERE user_id = ?', (self.__get_user_id(),))
            new_balance = cursor.fetchone()[0]
            conn.close()
        except Exception as e:
            return e
        return f'Your balance was down with {amount} uah\nCurrent balance: {new_balance}\n'

    def admin_rules(self):
        if self.username == 'admin':
            return True
        else:
            return False

    # get 10% bonus chance
    def get_bonus(self):
        chance = random.random()
        if chance < 0.1:
            self.top_up_balance(0.1 * self.check_user_balance())
            return 'Congratulations! You received 10% bonus on your balance!'
