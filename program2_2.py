print('Lesson 2_2: Поменять местами 0-1, 2-3, ... ')

list_any_elements = list(input('Input list of any elements separated by comma (,) 1,2,3...: ').split (","))

i = 1
# Сдвигаемся на 2 элемента пока не выйдем за конец списка. Последний нечетный не попадет в цикл
while i < len(list_any_elements):
    list_any_elements[i - 1], list_any_elements[i] = list_any_elements[i], list_any_elements[i-1]
    i += 2

print (list_any_elements)


