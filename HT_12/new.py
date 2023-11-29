def min_nominal_recursive(amount, bills, counts, memo):
    if amount == 0:
        return 0, {}
    if amount < 0:
        return float('inf'), {}

    if amount in memo:
        return memo[amount]

    min_count = float('inf')
    min_combination = {}

    for i, bill in enumerate(bills):
        if counts[i] > 0:
            counts[i] -= 1
            count, combination = min_nominal_recursive(amount - bill, bills, counts, memo)
            counts[i] += 1

            if count + 1 < min_count:
                min_count = count + 1
                min_combination = combination.copy()
                if bill in min_combination:
                    min_combination[bill] += 1
                else:
                    min_combination[bill] = 1

    memo[amount] = (min_count, min_combination)
    return min_count, min_combination

def min_nominal(bills, total_amount, bill_counts):
    memo = {}
    min_count, combination = min_nominal_recursive(total_amount, bills, bill_counts, memo)

    if min_count == float('inf'):
        return {}
    else:
        return combination


banknotes = [10, 20, 50, 100, 200, 500, 1000]
banknote_counts = [5, 1, 1, 0, 4, 1, 5]
cash_out_amount = 1170

result = min_nominal(banknotes, cash_out_amount, banknote_counts)
if result:
    for bill, count in result.items():
        print(f"{count}x{bill}")
else:
    print("Неможливо здійснити видачу з заданими купюрами.")