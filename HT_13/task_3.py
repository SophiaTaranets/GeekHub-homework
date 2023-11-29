# Створіть клас в якому буде атребут який буде рахувати кількість створених екземплярів класів.

class CounterClass:
    count = 0

    def __init__(self):
        CounterClass.count += 1


test_1 = CounterClass()
print(test_1.count)

test_2 = CounterClass()
print(test_2.count)

test_3 = CounterClass()
print(test_3.count)

