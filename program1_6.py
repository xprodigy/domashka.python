print('Lesson 1_5')

while True:
    a = input("Current result (km):")
    # валидация ввода
    # если в a не цифры, то до float(a) выполнение не дойдет и ошибка не возникнет
    if a.isnumeric() and 0 < float(a) <= 9999999999:
        a = float(a)

        while True:
            b = input("Needed result:")
            # валидация ввода
            # если в b не цифры, то до float(b) выполнение не дойдет и ошибка не возникнет
            if b.isnumeric() and 0 < float(b) <= 9999999999:
                b = float(b)

                day_number = 1  # переменная для хранения номера дня
                while a < b:  # проверяем результат на текущий день, если недостаточно -
                    day_number += 1  # переходим в след. день
                    a += a * 0.1  # добавляем 10% соответственно
                print("Day then result will reach", b, "km is", day_number)
                break

            # конец валидации ввода
            else:
                print('Invalid input. Retype')
                continue

        break

    # конец валидации ввода
    else:
        print('Invalid input. Retype')
        continue
