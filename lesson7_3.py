print('Lesson 7_3:')

class Cell:

    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return self.number + other.number

    def __sub__(self, other):
        return (self.number - other.number) if self.number > other.number else "Вычитание невозможно"

    def __mul__(self, other):
        return self.number * other.number

    def __truediv__(self, other):
        return f"{self.number / other.number:.0f}"

    def make_order(self, row):
        j = 1
        out_string = ''
        for i in range(self.number):
            if j < row:
                out_string += '*'
                j += 1
            else:
                out_string += '*\n'
                j = 1
        return out_string


cell1 = Cell(44)
cell2 = Cell(7)

print(f"Cумма клеток 1 + 2 = {cell1 + cell2}")
print(f"Разность клеток 1 - 2 = {cell1 - cell2}")
print(f"Разность клеток 2 - 1 = {cell2 - cell1}")
print(f"Произведеение клеток 1 * 2 = {cell1 * cell2}")
print(f"Разность клеток 1 / 2 = {cell1 / cell2}")

print(f"Клетка 1\n{cell1.make_order(15)}")
print(f"Клетка 2\n{cell2.make_order(4)}")
