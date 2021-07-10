print('Lesson 8_7')


# таки не понял смысл задачи.. Сделать перегрузку метода, чтобы получить тот же самый результат?


class MyComlex:
    def __init__(self, num):
        self.complex_num = num

    def __mul__(self, other):
        return MyComlex(self.complex_num * other.complex_num)

    def __add__(self, other):
        return MyComlex(self.complex_num + other.complex_num)

    def __str__(self):
        return str(self.complex_num)


arg_1 = MyComlex(-10 + 0.1j)
arg_2 = MyComlex(23.5 - 2.1j)
arg_3 = MyComlex(1.5 - 1.1j)
arg_4 = MyComlex(1.2 + 2.1j)

print(arg_1 * arg_2)
print(arg_1 + arg_2)
print(arg_1 * arg_2 + arg_3 * arg_4)
