# Write a script which accepts a <number> from user and then <number> times asks user for string input.
# At the end script must print out result of concatenating all <number> strings.

number = int(input('Enter number: '))
lst = []
for i in range(number):
    s = input(f'Enter {i+1} number: ')
    lst.append(s)
print('Result:', ''.join(lst))
