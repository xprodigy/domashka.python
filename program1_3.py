print('Lesson 1_3')

while True:
    n = input("Enter number n (0 - 100000): ")
    if n.isdigit() and 0 <= int(n) <= 100000:
        # если в n не цифры, то до int(n) выполнение не дойдет и ошибка не возникнет
        print("n + nn + nnn =", f"{n} + {n + n} + {n + n + n} =", int(n) + int(n + n) + int(n + n + n))
        break
    else:
        print('Invalid input. Retype')
        continue

