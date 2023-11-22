import sqlite3
import Validation


def check_bank_nominal():
    try:
        conn = sqlite3.connect('bank.db')
        cursor = conn.cursor()
        cursor.execute('SELECT nominal_10, '
                       'nominal_20, '
                       'nominal_50, '
                       'nominal_100,'
                       'nominal_200, '
                       'nominal_500, '
                       'nominal_1000 FROM bank_account WHERE id = 1')
        nominal_tuple = cursor.fetchone()

        nominal_dict = {
            '10': nominal_tuple[0],
            '20': nominal_tuple[1],
            '50': nominal_tuple[2],
            '100': nominal_tuple[3],
            '200': nominal_tuple[4],
            '500': nominal_tuple[5],
            '1000': nominal_tuple[6]
        }

        conn.close()
    except Exception as e:
        return e
    else:
        return nominal_dict


def update_bank_balance():
    nominal_dict = check_bank_nominal()
    balance = 0
    for nominal, nominal_value in nominal_dict.items():
        balance += int(nominal) * nominal_value

    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE bank_account SET total_balance = ?', (balance,))
    conn.commit()


def check_bank_balance():
    update_bank_balance()
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    cursor.execute('SELECT total_balance FROM bank_account')
    balance = cursor.fetchone()[0]
    return balance


def add_bank_nominal(nominal, new_count):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    if nominal == 10:
        cursor.execute('UPDATE bank_account SET nominal_10 = nominal_10 + ?', (new_count,))
        conn.commit()
    elif nominal == 20:
        cursor.execute('UPDATE bank_account SET nominal_20 = nominal_20 + ?', (new_count,))
        conn.commit()
    elif nominal == 50:
        cursor.execute('UPDATE bank_account SET nominal_50 = nominal_50 + ?', (new_count,))
        conn.commit()
    elif nominal == 100:
        cursor.execute('UPDATE bank_account SET nominal_100 = nominal_100 + ?', (new_count,))
        conn.commit()
    elif nominal == 200:
        cursor.execute('UPDATE bank_account SET nominal_200 = nominal_200 + ?', (new_count,))
        conn.commit()
    elif nominal == 500:
        cursor.execute('UPDATE bank_account SET nominal_500 = nominal_500 + ?', (new_count,))
        conn.commit()
    elif nominal == 1000:
        cursor.execute('UPDATE bank_account SET nominal_1000 = nominal_1000 + ?', (new_count,))
        conn.commit()
    conn.close()


def subtract_bank_nominal(nominal, new_count):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    nominal_dict = check_bank_nominal()
    current_nominal_value = nominal_dict[str(nominal)]

    if new_count > current_nominal_value:
        raise Validation.ValidationException('Bank does not have enough banknotes of this nominal')
    else:
        if nominal == 10:
            cursor.execute('UPDATE bank_account SET nominal_10 = nominal_10 - ?', (new_count,))
            conn.commit()
        elif nominal == 20:
            cursor.execute('UPDATE bank_account SET nominal_20 = nominal_20 - ?', (new_count,))
            conn.commit()
        elif nominal == 50:
            cursor.execute('UPDATE bank_account SET nominal_50 = nominal_50 - ?', (new_count,))
            conn.commit()
        elif nominal == 100:
            cursor.execute('UPDATE bank_account SET nominal_100 = nominal_100 - ?', (new_count,))
            conn.commit()
        elif nominal == 200:
            cursor.execute('UPDATE bank_account SET nominal_200 = nominal_200 - ?', (new_count,))
            conn.commit()
        elif nominal == 500:
            cursor.execute('UPDATE bank_account SET nominal_500 = nominal_500 - ?', (new_count,))
            conn.commit()
        elif nominal == 1000:
            cursor.execute('UPDATE bank_account SET nominal_1000 = nominal_1000 - ?', (new_count,))
            conn.commit()
        conn.close()
