print('Lesson 4_7')


def fact(n):
    y = 1
    for f in range(1, n+1):
        y = y * f
        yield y


n = int(input('Для скольких первых n чисел посчитать факториалы?:'))

for el in fact(n):
    print(el)

