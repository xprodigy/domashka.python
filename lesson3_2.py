print('Lesson 3_2:')


def my_func(**kwargs):
    return ', '.join(kwargs.values())


list = list(input('Name, surname, year of birth, city, email, phone:\n(Six words separated by space)\n').split(" "))

print(my_func(name=list[0], surname=list[1], year=list[2], city=list[3], email=list[4], phone=list[5]))
