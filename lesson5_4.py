print('Lesson 5_4:')

rus_file = open("rus.txt", 'w', encoding="utf-8")

dictionary = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open("eng_rus.txt", encoding="utf-8") as f_obj:
    for el in f_obj.readlines():
        i = el.split()
        rus_file.write(dictionary.get(i[0]) + ' ' + i[1] + ' ' + i[2] + '\n')
    rus_file.close()
