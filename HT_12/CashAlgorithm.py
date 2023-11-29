from Bank import Bank


def min_nominal(banknote_dict, total_amount):
    def min_nominal_recursive(amount, memo):
        if amount == 0:
            return 0, {}
        if amount < 0:
            return float('inf'), {}

        if amount in memo:
            return memo[amount]

        min_count = float('inf')
        min_combination = {}

        for bill, count in banknote_dict.items():
            if count > 0:
                banknote_dict[bill] -= 1
                sub_count, sub_combination = min_nominal_recursive(amount - bill, memo)
                banknote_dict[bill] += 1

                if sub_count + 1 < min_count:
                    min_count = sub_count + 1
                    min_combination = sub_combination.copy()
                    if bill in min_combination:
                        min_combination[bill] += 1
                    else:
                        min_combination[bill] = 1

        memo[amount] = (min_count, min_combination)
        return min_count, min_combination

    memo = {}
    min_count, combination = min_nominal_recursive(total_amount, memo)

    if min_count == float('inf'):
        return {}
    else:
        return combination


def change_db_nominal(banknote_dict, amount):
    result = min_nominal(banknote_dict, amount)
    b = Bank()
    if result:
        for coin, count in result.items():
            b.subtract_bank_nominal(coin, count)
        b.update_bank_balance()

        print('Banknotes: ')
        for bill, count in result.items():
            print(f"{count}x{bill}")
    else:
        print("Cannot make the exact amount.")


def get_min_nom(banknot, amount):
    result = min_nominal(banknot, amount)
    if result:
        for bill, count in result.items():
            print(f"{count}x{bill}")
    else:
        print("Cannot make the exact amount.")

# Test 1: 1170
# banknote_dict = {1000: 5, 500: 1, 200: 4, 100: 0, 50: 1, 20: 1, 10: 5}
# cash_out_amount = 1170
# get_min_nom(banknote_dict, cash_out_amount)

# Test 2: 160
# banknote_dict = {1000: 5, 500: 1, 200: 4, 100: 10, 50: 10, 20: 10, 10: 0}
# cash_out_amount = 160
# get_min_nom(banknote_dict, cash_out_amount)

# Test 3: 110
# banknote_dict =  {1000: 5, 500: 1, 200: 1, 100: 1, 50: 4, 20: 6, 10: 0}
# cash_out_amount = 110
# get_min_nom(banknote_dict, cash_out_amount)
