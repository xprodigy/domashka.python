print('Lesson 7_1:')


class Matrix:

    def __init__(self, list_matrix):
        self.list_matrix = list_matrix

    def __add__(self, other):
        self.result = []
        for i in range(len(self.list_matrix)):
            self.result.append(list(map(sum, zip(self.list_matrix[i], other.list_matrix[i]))))
        return '\n'.join(['\t'.join(map(str, i)) for i in self.result])

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, i)) for i in self.list_matrix])


matrix_1 = [[1, 3, 4, 29],
            [3, -4, 6, 1],
            [3, 4, 1, 24]]

matrix_2 = [[2, 0, 11, 5],
            [-3, 6, 1, 9],
            [18, 2, 7, -1]]

matrix_1 = Matrix(matrix_1)
matrix_2 = Matrix(matrix_2)

print(f"{matrix_1} \n")
print(f"{matrix_2} \n")

print(matrix_1 + matrix_2)
