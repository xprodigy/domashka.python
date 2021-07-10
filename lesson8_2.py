print('Lesson 8_2 Division by zero exept')


class ZeroDivErr(Exception):
    def __str__(self):
        return f'Division by zero'


a = input('Input 1st argument: ')
b = input('Input 2nd argument: ')
print('Division result:')

if a.isdigit():
    a = int(a)
else:
    a = ord(a)
if b.isdigit():
    b = int(b)
else:
    b = ord(b)

try:
    if b == 0:
        raise ZeroDivErr()
    else:
        print(a / b)
except ZeroDivErr as err:
    print(err)
