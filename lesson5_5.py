print('Lesson 5_5:')

import random

with open("num.txt", "w+") as f_obj: # открываем файлы
    for n in range(1, 50): # записыаем в него, например, 50 рандомных чисел, разделенных пробелами
        print(random.randint(1, 999), ' ', file=f_obj)

    f_obj.seek(0) # возвращаем указатель в начало
    print(sum(map(int, f_obj.readline().split()))) # считываем файл (он однострочный), разбиваем и сразу суммируем
