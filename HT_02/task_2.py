# Write a script which accepts two sequences of comma-separated colors from user.
# Then print out a set containing all the colors from color_list_1 which are not present in color_list_2.

color_list_1 = set(input('Enter the first color list: ').replace(' ', '').split(','))
color_list_2 = set(input('Enter the second color list: ').replace(' ', '').strip().split(','))
color_difference = color_list_1 - color_list_2
print('The colors from the first color list which are not present in the second color list: ', color_difference)
