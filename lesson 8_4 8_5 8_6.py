print('Lesson 8_4-8_6: Warehouse of office equipment')


class warehouses:

    def __init__(self):
        # set defaults
        self.owner = "IT-company"
        self.quantity = {'scanners': 0, 'printers': 0, 'copiers': 0}

    def __str__(self):
        return f"scanners {self.quantity['scanners']}, printers {self.quantity['printers']}," \
               f" copiers {self.quantity['copiers']}"

    def add(self, str):
        if str == 'q':
            return True
        str = str.split(" ")
        if len(str) == 2 and (str[0] == 'scanners' or str[0] == 'printers' or str[0] == 'copiers') and str[
            1].isdigit() and int(
            str[1]) > 0:
            self.quantity[str[0]] += int(str[1])
            print('Получено')
            return True
        else:
            print("Неверный ввод. Пример правильного ввода: printers 12")
            return False

    def send(self, obj, str):
        other = obj
        if str == 'q':
            return True
        str = str.split(" ")
        if len(str) == 2 and (str[0] == 'scanners' or str[0] == 'printers' or str[0] == 'copiers') and str[
            1].isdigit() and int(
            str[1]) > 0:

            if (self.quantity[str[0]] - int(str[1])) >= 0:
                self.quantity[str[0]] -= int(str[1])
                other.quantity[str[0]] += int(str[1])
                print('Отправлено')
            else:
                print('На складе нет столько техники')
                return False
            return True
        else:
            print("Неверный ввод. Пример правильного ввода: printers 12")
            return False


class office_equipment:
    voltage = 220
    frequency = 50


class printer(office_equipment):
    vendor = 'Canon'


class scanner(office_equipment):
    vendor = 'HP'


class copier(office_equipment):
    vendor = 'Xerox'


warehouse = warehouses()  # Создаем склад
in_office = warehouses()  # Создаем офис

while True:
    str_in = input(
        f"1. Посмотреть количество техники\n2. Получить новую технику на склад\n"
        f"3. Отправить технику со склада в офис\nq. Выход\n>>> ")
    if str_in == '1':
        print('=' * 60, f'\nКоличество на складе: {warehouse}.\nКоличество в офисе: {in_office}.\n', '=' * 60, '\n',
              sep='')
    if str_in == '2':
        while True:
            if warehouse.add(
                    input(
                        'Получить | Введите название (scanners/printers/copiers) и кол-во через пробел. Выход - q: ')):
                break

    if str_in == '3':
        while True:
            if warehouse.send(in_office, input(
                    'Отправить | Введите название (scanners, printers, copiers) и кол-во через пробел. Выход - q: ')):
                break

    if str_in == 'q':
        break
