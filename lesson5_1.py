print('Lesson 5_1:')

new_file = open("text.txt", 'w', encoding="utf-8")

while True:
    str = input('Введите строку для файла text.txt, либо Enter для завершения работы:\n')
    if str != '':
        new_file.write(str + '\n')
    else:
        new_file.close()
        break
