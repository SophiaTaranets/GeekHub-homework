# Банкомат 3.0
# - реалізуйте видачу купюр за логікою видавання найменшої кількості купюр. Наприклад: 2560 --> 2х1000, 1х500, 3х20.
# Будьте обережні з "жадібним алгоритмом"!

import sqlite3
import math
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

    def sorted_nominal(self):
        nominal_dict = self.check_bank_nominal()
        sorted_nominal_dict = sorted(nominal_dict.items(), key=lambda n: n[1], reverse=True)

        return dict(sorted_nominal_dict)

    def get_needed_banknotes(self, needed_money: int) -> dict:
        """Get atm banknotes with the smallest amount of banknotes using recursion with memoization

        Returns dict {"change": int, "used_banknotes": [{'denomination': int}, 'amount': int], ...}

        If needed_money is less than the smallest available denomination:
        returns dict {"change": needed_money, "used_banknotes": []}
        """

        # Отримання відсортованого словника номіналів банкнот
        sorted_nominals = self.sorted_nominal()

        # Створення списку банкнот із відсортованими номіналами
        banknotes = [{"denomination": int(denomination), "amount": sorted_nominals[denomination]} for denomination in
                     sorted_nominals.keys()]

        # Кількість різних номіналів банкнот
        len_banknotes = len(banknotes)

        # Helper function using recursion with memoization
        def helper(target: int, index: int = 0, memo: dict = {}):

            # Вхідні параметри та логіка функції-допоміжника залишається без змін

            # Виклик функції-допоміжника для отримання результату
            remaining, count, used_banknotes = helper(target=needed_money)

            # Перевірка, чи вдалося знайти комбінацію
            if count == float("inf"):
                return {"change": needed_money, "used_banknotes": []}
            else:
                return {"change": remaining, "used_banknotes": used_banknotes}

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

    def withdraw_cash(self, user_sum):
        # Check if the user_sum is greater than the ATM balance
        if user_sum > self.check_bank_balance():
            raise Validation.ValidationException('ATM does not have enough funds for withdrawal')

        # Get the banknotes available in the ATM
        banknotes = self.check_bank_nominal()

        # Sort the banknotes in descending order
        sorted_banknotes = sorted(banknotes.items(), key=lambda x: int(x[0]), reverse=True)

        # Initialize a result list to store the dispensing result
        result = []

        # Iterate through the sorted banknotes
        for denomination, available_count in sorted_banknotes:
            denomination = int(denomination)
            available_count = int(available_count)

            # Calculate the number of banknotes needed for the current denomination
            needed_count = user_sum // denomination

            # Determine the actual number of banknotes to dispense
            dispense_count = min(needed_count, available_count)

            # Update the user_sum and available_count
            user_sum -= dispense_count * denomination
            available_count -= dispense_count

            # Add the result to the list
            result.append((denomination, dispense_count))

            # Update the available count in the ATM
            self.subtract_bank_nominal(denomination, dispense_count)

            # If the user_sum becomes 0, break the loop
            if user_sum == 0:
                break

        # Check if the ATM has enough funds for the dispensing
        if user_sum > 0:
            raise Validation.ValidationException('ATM does not have enough funds for withdrawal')

        # Return the dispensing result
        return result

b = Bank()
print(b.get_needed_banknotes(110))

