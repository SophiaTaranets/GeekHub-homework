# Write a script which accepts a <number> from user and print out a sum of the first <number> positive integers.

number = int(input('Enter number: '))
suma = 0
for i in range(1, number + 1):
    suma += i
print(f'Sum of the first {number} positive integers: {suma}')
