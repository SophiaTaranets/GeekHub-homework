# Write a script to concatenate all elements in a list into a string and print it.
# List must be include both strings and integers and must be hardcoded.

lst = ['geethub', 2023]
st = ''
for i in range(len(lst)):
    st += f'{lst[i]}'
print(st)
