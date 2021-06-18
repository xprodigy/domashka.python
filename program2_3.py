print('Lesson 2_3: зима, весна, лето, осень')

month = int(input('Type month number (1-12): '))

print('Resolve with LIST:')
db_list = ['Winter', 'Winter', 'Spring', 'Spring', 'Spring',
      'Summer', 'Summer', 'Summer', 'Autumn', 'Autumn', 'Autumn', 'Winter']

print('Season of month number', month, 'is', db_list[month - 1])

print('Resolve with DICT:')
db_dict = {1: 'Winter', 2: 'Winter', 3: 'Spring',4: 'Spring', 5: 'Spring', 6: 'Summer', 7: 'Summer',
           8: 'Summer', 9: 'Autumn', 10: 'Autumn', 11: 'Autumn',  12: 'Winter'}

print('Season of month number', month, 'is', db_dict[month])

