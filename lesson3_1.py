print('Lesson 3_1')


def my_func_division(arg1, arg2):
    try:
        result = int(arg1) / int(arg2)
    except (ValueError, ZeroDivisionError) as result:
        return result
    return result


a = input('Input 1st argument:')
b = input('Input 2nd argument:')

print('Division result:', my_func_division(a, b))
