# Write a script to concatenate following dictionaries to create a new one.
dict_1 = {'foo': 'bar', 'bar': 'buz'}
dict_2 = {'dou': 'jones', 'USD': 36}
dict_3 = {'AUD': 19.2, 'name': 'Tom'}

concatenated_dict = {**dict_1, **dict_2, **dict_3}
print(f'Concatenated dict: {concatenated_dict}')
