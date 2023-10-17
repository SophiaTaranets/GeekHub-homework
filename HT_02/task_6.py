# Write a script to check whether a value from user input is contained in a group of values.
# e.g. [1, 2, 'u', 'a', 4, True] --> 2 --> True
#      [1, 2, 'u', 'a', 4, True] --> 5 --> False

lst1 = [1, 2, 'u', 'a', 4, True]
str_lst1 = [str(i) for i in lst1]
value = input('Enter value: ')
print(value in str_lst1)
