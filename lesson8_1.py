print('Lesson 8_1:')


class date:

    @classmethod  # Метод, конвертирующий строковую дату в числа
    def date_to_int(cls, date_str):
        if date.date_validation(date_str):
            return f"Converted to int: {list(map(int, date_str.split('-')))}"
        else:
            return "The format of the entered date is incorrect!"

    @staticmethod  # Метод, проводящий валидацию формата введенной даты
    def date_validation(date_val):  # если isdigit не сработает, до преобразования int не дойдет и ошибка не возникнет
        return date_val[:2].isdigit() and 0 < int(date_val[:2]) < 32 and date_val[2:3] == '-' and date_val[3:5].isdigit(
        ) and 0 < int(date_val[3:5]) < 13 and date_val[5:6] == '-' and date_val[6:8].isdigit()


data_obj = print(date.date_to_int(input("Input date as dd-mm-yy: ")))
