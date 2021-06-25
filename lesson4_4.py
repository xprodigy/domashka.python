print('Lesson 4_4:')

source_list = [0, 2, 2, 7, 23, 1, 44, 44, 3, 3, 2, 10, 7, 4, 11, 234, 2345, 25, 26, 26, 27, 28, 0, 2222]

result_list = [source_list[i] for i in range(0, len(source_list)) if (source_list[i] not in source_list[:i]) and
               (source_list[i] not in source_list[i + 1:])]

print('Исходный список:', *source_list)
print('Результат:', *result_list)
