print('Lesson 4_1:')

# for example: python lesson4_1.py 123 10 100

from sys import argv

_, first_param, second_param, third_param = argv

print("\nВыработка:", first_param)
print("Ставка в час:", second_param)
print("Премия:", third_param)
print("-" * 20 + "\nЗаработная плата:", int(first_param) * int(second_param) + int(third_param), "\n")
