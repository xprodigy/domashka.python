print('Lesson 4_6')

from itertools import count, cycle


for el in count(int(input('Script 1\nВведите первое число для генератора (1..9):'))):
    if el >= 10:
        break
    else:
        print(el, ' ', end=' ')


print ('\n\nScript 2')
smile = [":)", ' ']
smile_count = int(input('Сколько смайлов нарисовать? (1..10000):'))
i=0
j=0
while i < smile_count:
    for el in cycle(smile):
        print(el, end='')
        j += 1
        i += 1
        if j > 50 or i > smile_count:
            break
    print('')
    j = 0

