import sqlite3


def check_bank_balance():
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    cursor.execute('SELECT total_balance FROM bank_account')
    balance = cursor.fetchone()
    conn.close()
    return balance


def top_up_bank_balance(amount):
    try:
        conn = sqlite3.connect('bank.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE bank_account SET total_balance = total_balance + ?', (amount,))
        conn.commit()

        cursor.execute('SELECT total_balance FROM bank_account', ())
        balance = cursor.fetchone()
        conn.close()

    except Exception as e:
        return e
    return f'Bank balance was replenished with {amount} uah\nCurrent balance: {balance}\n'


def check_bank_nominal():
    try:
        conn = sqlite3.connect('bank.db')
        cursor = conn.cursor()
        cursor.execute('SELECT nominal_10, '
                       'nominal_20, '
                       'nominal_50, '
                       'nominal_100,'
                       'nominal_200, '
                       'nominal_500 FROM bank_account WHERE id = 1')
        nominal_tuple = cursor.fetchone()

        nominal_dict = {
            '10': nominal_tuple[0],
            '20': nominal_tuple[1],
            '50': nominal_tuple[2],
            '100': nominal_tuple[3],
            '200': nominal_tuple[4],
            '500': nominal_tuple[5]
        }

        conn.close()
    except Exception as e:
        return e
    else:
        return nominal_dict


def change_bank_nominal(nominal, new_count):
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
    conn.close()
    return f'Bank nominal was successfully changed: {check_bank_nominal()}\n'
