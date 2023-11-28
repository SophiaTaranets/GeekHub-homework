from Bank import Bank
from Validation import BanknoteException


def min_coins(nom_dict, amount, memo={}):
    filtered_coins = {key: value for key, value in nom_dict.items() if value != 0}
    coin_values = filtered_coins.keys()

    if amount == 0:
        return 0, {}

    if amount < 0:
        return float('inf'), {}

    if amount in memo:
        return memo[amount]

    min_count = float('inf')
    min_count_coins = {}

    for coin in coin_values:
        remaining_target = amount - coin
        count, remaining_coins = min_coins(nom_dict, remaining_target, memo)
        count += 1

        if count < min_count:
            min_count = count
            min_count_coins = remaining_coins.copy()
            min_count_coins[coin] = min_count_coins.get(coin, 0) + 1

    memo[amount] = min_count, min_count_coins
    return min_count, min_count_coins


def change_db_nominal(banknote_dict, amount):
    min_count, min_coins_used = min_coins(banknote_dict, amount)
    b = Bank()
    if min_count == float('inf'):
        raise BanknoteException("Cannot make the exact amount.")
    else:
        for coin, count in min_coins_used.items():
            b.subtract_bank_nominal(coin, count)
            b.update_bank_balance()


def get_min_coins(banknote_dict, amount):
    min_count, min_coins_used = min_coins(banknote_dict, amount)

    if min_count == float('inf'):
        raise BanknoteException("Cannot make the exact amount.")
    else:
        print_result = []
        for coin, count in min_coins_used.items():
            print_result.append(f"{count} x {coin}")
        return print_result


# # Test 1: 1170
# banknote_dict = {1000: 5, 500: 1, 200: 4, 100: 0, 50: 1, 20: 1, 10: 5}
# amount = 1170
# print(f'1170 -->')
# get_min_coins(banknote_dict, amount)
#
# print('-' * 15)
#
# # Test 2: 160
# banknote_dict = {1000: 5, 500: 1, 200: 4, 100: 10, 50: 10, 20: 10, 10: 0}
# amount = 160
# print(f'160 -->')
# get_min_coins(banknote_dict, amount)
#
# print('-' * 15)
#
# # Test 3: 110
# banknote_dict = {1000: 5, 500: 1, 200: 1, 100: 1, 50: 4, 20: 6, 10: 0}
# amount = 110
# print(f'110 -->')
# get_min_coins(banknote_dict, amount)
