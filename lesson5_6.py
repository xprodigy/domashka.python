print('Lesson 5_6')

num_str = ''
sum = 0
dictionary = {}

with open("lessons_quantity.txt", encoding="utf-8") as f_obj:
    for el in f_obj.readlines(): # читаем файл построчно
        for i in el:              # внутри каждой строки двигаемся посимвольно
            if i.isdigit():        # если попадаются цифры -
                num_str += i        # составляем подстроку из последовательно идущих цифр
            elif len(num_str) > 0:   # в противном случае смотрим накопились ли цифры в подстроке, если да, то
                sum = sum + int(num_str)   # увеличиваем общую сумму занятий на это число и
                num_str = ''               # освобождаем подстроку для поиска следующей последовательности цифр
        dictionary.update({el[:(el.find(':'))]: sum})  # получившуюся общую сумму занятий записываем в словарь
        sum = 0                                        # освобождаем переменную

print(dictionary)
