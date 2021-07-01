print('Lesson 6_3:')


class Worker:

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


junior_1 = Position('Bob', "Jonson", 'junior', {'wage': 10000, 'bonus': 3800})
middle_1 = Position('Dew', "Robinson", 'middle', {'wage': 16000, 'bonus': 6500})

print(junior_1.get_full_name(), ': position is ', junior_1.position, ', total income is ', junior_1.get_total_income(),
      sep='')
print(middle_1.get_full_name(), ': position is ', middle_1.position, ', total income is ', middle_1.get_total_income(),
      sep='')
