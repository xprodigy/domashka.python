print('Lesson 3_3:')


def my_func(arg1, arg2, arg3):
    try:
        result = int(arg1) + int(arg2) + int(arg3) - min(int(arg1), int(arg2), int(arg3))
    except (ValueError) as result:
        return result
    return result


a = input('Input 1st argument:')
b = input('Input 2nd argument:')
c = input('Input 3rd argument:')

print('Sum of two biggest:', my_func(a, b, c))
