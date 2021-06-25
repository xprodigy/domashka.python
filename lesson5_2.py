print('Lesson 5_2:')

with open("films.txt", encoding="utf-8") as f_obj:
    i = 0
    for line in f_obj:
        i += 1
        print('Кол-во слов в строке №', i, ':', len(line.split()))
    print('Всего строк:', i)
