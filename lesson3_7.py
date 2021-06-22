print('Lesson 3_7')


def int_func(str1):
    return (str1.title())


def word_func(str1):
    result = ''
    for word in str1.split():
        result = result + int_func(word) + ' '
    print(result)


word_func(input('Enter string:'))
