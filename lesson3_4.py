print('Lesson 3_4. x ** y')


def my_func(x, y):
    try:
        result = int(x) ** int(y)
    except (ValueError, TypeError) as result:
        return result
    return result

def my_func_v2(x, y):
    result = 1
    try:
        y = int(y)
        while y < 0:
            result = result / int(x)
            y += 1
    except (ValueError, TypeError) as result:
            return result
    return result

x = input('Input x:')
y = input('Input y:')

print ('Try with "**":', my_func(x, y))
print ('Try with cycle "while":', my_func_v2(x, y))
