import sqlite3
import Validation


class Bank:
    def __init__(self):
        self.conn = sqlite3.connect('bank.db')
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def check_bank_nominal(self):
        try:
            self.cursor.execute('SELECT nominal_10, '
                           'nominal_20,'
                           'nominal_50,'
                           'nominal_100,'
                           'nominal_200,'
                           'nominal_500, '
                           'nominal_1000 FROM bank_account WHERE id = 1')
            nominal_tuple = self.cursor.fetchone()

            nominal_dict = {
                '10': nominal_tuple[0],
                '20': nominal_tuple[1],
                '50': nominal_tuple[2],
                '100': nominal_tuple[3],
                '200': nominal_tuple[4],
                '500': nominal_tuple[5],
                '1000': nominal_tuple[6]
            }

        except Exception as e:
            return e
        else:
            return nominal_dict

    def update_bank_balance(self):
        nominal_dict = self.check_bank_nominal()
        balance = 0
        for nominal, nominal_value in nominal_dict.items():
            balance += int(nominal) * nominal_value

        self.cursor.execute('UPDATE bank_account SET total_balance = ?', (balance,))
        self.conn.commit()

    def check_bank_balance(self):
        self.update_bank_balance()
        self.cursor.execute('SELECT total_balance FROM bank_account')
        balance = self.cursor.fetchone()[0]
        return balance

    def add_bank_nominal(self, nominal, new_count):
        if nominal == 10:
            self.cursor.execute('UPDATE bank_account SET nominal_10 = nominal_10 + ?', (new_count,))
            self.conn.commit()
        elif nominal == 20:
            self.cursor.execute('UPDATE bank_account SET nominal_20 = nominal_20 + ?', (new_count,))
            self.conn.commit()
        elif nominal == 50:
            self.cursor.execute('UPDATE bank_account SET nominal_50 = nominal_50 + ?', (new_count,))
            self.conn.commit()
        elif nominal == 100:
            self.cursor.execute('UPDATE bank_account SET nominal_100 = nominal_100 + ?', (new_count,))
            self.conn.commit()
        elif nominal == 200:
            self.cursor.execute('UPDATE bank_account SET nominal_200 = nominal_200 + ?', (new_count,))
            self.conn.commit()
        elif nominal == 500:
            self.cursor.execute('UPDATE bank_account SET nominal_500 = nominal_500 + ?', (new_count,))
            self.conn.commit()
        elif nominal == 1000:
            self.cursor.execute('UPDATE bank_account SET nominal_1000 = nominal_1000 + ?', (new_count,))
            self.conn.commit()

    def subtract_bank_nominal(self, nominal, new_count):
        nominal_dict = self.check_bank_nominal()
        current_nominal_value = nominal_dict[str(nominal)]

        if new_count > current_nominal_value:
            raise Validation.ValidationException('Bank does not have enough banknotes of this nominal')
        else:
            if nominal == 10:
                self.cursor.execute('UPDATE bank_account SET nominal_10 = nominal_10 - ?', (new_count,))
                self.conn.commit()
            elif nominal == 20:
                self.cursor.execute('UPDATE bank_account SET nominal_20 = nominal_20 - ?', (new_count,))
                self.conn.commit()
            elif nominal == 50:
                self.cursor.execute('UPDATE bank_account SET nominal_50 = nominal_50 - ?', (new_count,))
                self.conn.commit()
            elif nominal == 100:
                self.cursor.execute('UPDATE bank_account SET nominal_100 = nominal_100 - ?', (new_count,))
                self.conn.commit()
            elif nominal == 200:
                self.cursor.execute('UPDATE bank_account SET nominal_200 = nominal_200 - ?', (new_count,))
                self.conn.commit()
            elif nominal == 500:
                self.cursor.execute('UPDATE bank_account SET nominal_500 = nominal_500 - ?', (new_count,))
                self.conn.commit()
            elif nominal == 1000:
                self.cursor.execute('UPDATE bank_account SET nominal_1000 = nominal_1000 - ?', (new_count,))
                self.conn.commit()
