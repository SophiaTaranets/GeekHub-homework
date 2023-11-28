def min_nominal(bills, total_amount, bill_counts):
    min_bills_list = [0] + [float('inf')] * total_amount
    used_bills = {current_amount: None for current_amount in range(total_amount + 1)}

    for bill, count in zip(bills, bill_counts):
        for amount in range(bill, total_amount + 1):
            if min_bills_list[amount - bill] + 1 < min_bills_list[amount]:
                min_bills_list[amount] = min_bills_list[amount - bill] + 1
                used_bills[amount] = bill

    if min_bills_list[total_amount] == float('inf'):
        return {}
    else:
        result = {}
        while total_amount > 0:
            bill = used_bills[total_amount]
            result[bill] = result.get(bill, 0) + 1
            total_amount -= bill

        return result

if __name__ == "__main__":
    banknotes = [10, 20, 50, 200, 500, 1000]
    banknote_counts = [5, 1, 1, 4, 1, 5]
    cash_out_amount = 1170

    print(min_nominal(banknotes, cash_out_amount, banknote_counts))
