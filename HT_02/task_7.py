# Write a script to concatenate all elements in a list into a string and print it.
# List must be include both strings and integers and must be hardcoded.

lst = ['geethub', 2023]
str_lst = [str(i) for i in lst]
print(''.join(str_lst))
