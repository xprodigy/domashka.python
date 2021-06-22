print('Lesson 3_5')


def my_func(list, sum):
    try:
        for i in list:
            if i == 'q':
                return [sum, False]
            else:
                sum += int(i)
        return [sum, True]
    except (ValueError, TypeError) as err:
        return [err, False]


list = input('Input numbers separated by space and q instead of the last:\n'
             'For example: 3 231 31\nFor example: 3365 2 463 q\n>').split(" ")
result = [0, False]

while True:
    result = my_func(list, result[0])
    print('Current sum:', result[0])
    if result[1] == True:
        list = input('Enter more >').split(" ")

    else:
        result = my_func(list, result[0])
        break
