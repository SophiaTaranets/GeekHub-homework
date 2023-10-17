# Write a script which accepts a sequence of comma-separated numbers
# from user and generate a list and a tuple with those numbers.

numbers = input('Enter a sequence of comma-separated numbers: ').replace(' ', '').split(',')
numbers = [int(i) for i in numbers]
print('List: ', numbers)
print('Tuple: ', tuple(numbers))
