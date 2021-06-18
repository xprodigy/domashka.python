print('Lesson 2_6 Товары')

# Если лень вводить с клавиатуры - вот готовый ввод:
#
# products = [
#     (1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
#     (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
#     (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})
# ]

print ('Введите название, цену, количество, ед.изм через пробел или q для выхода')
print ('Например: принтер 2500 5 шт \n')
i = 1

products = [] # если не обьявить - в цикле будет ошибка NameError: name 'products' is not defined

while True:
    string = input(f"Продукт №'{i}:")
    if string == 'q':
        break
    else:
        string = list(string.split())
        products.append((i, {"название": string[0], "цена": string[1], "количество": string[2], "eд": string[3]}))
        i += 1


# dictionary обьявляю заранее иначе внутри цикла - NameError: name 'dictionary' is not defined
dictionary = {"название": [], "цена": [], "количество": [], "eд": []}

 # парсинг
for i, element in enumerate(products):
    dictionary["название"].append(element[1]["название"])
    dictionary["цена"].append(element[1]["цена"])
    dictionary["количество"].append(element[1]["количество"])
    dictionary["eд"].append(element[1]["eд"])

# вывод результата
print('\nАналитика:\n',dictionary)
