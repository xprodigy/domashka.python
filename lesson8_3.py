print('Lesson 8_3')


class not_numeric(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return f'Warning! Element "{self.msg}" is not numeric'


list_in = input('Input numbers separated by space and q instead of the last:\n'
                'For example: 3 231 31\nFor example: 3365 2 463 q\n>').split(" ")

list_out = []
stop = False

while True:
    for el in list_in:
        if el == 'q':
            print(list_out)
            stop = True
            break
        elif el.isdigit():
            list_out.append(int(el))
        elif el == '':
            continue
        else:
            try:
                raise not_numeric(el)
            except not_numeric as err:
                print(err)
    if stop:
        break
    list_in = input('Enter more >').split(" ")
