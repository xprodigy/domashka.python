print('Lesson 1_5')

while True:

    revenue = input("How much revenue your business received? : ")
    # валидация ввода:
    # если в revenue не цифры, то до int(revenue) выполнение не дойдет и ошибка не возникнет
    if revenue.isdigit() and 0 <= int(revenue) <= 999999999999:
        revenue = int(revenue)
        while True:

            cost = input("How much cost of your business? : ")
            # валидация ввода:
            # если в cost не цифры, то до int(cost) выполнение не дойдет и ошибка не возникнет
            if cost.isdigit() and 0 <= int(cost) <= 999999999999:
                cost = int(cost)

                fin_result = revenue - cost  # получили результат затем 3 варианта ответа на него

                if fin_result > 0:
                    print("Good work, your profit is ", fin_result, "!", sep="")
                    print("Profitability is", f"{100 * fin_result / revenue:.1f}%")

                    while True:

                        employees = input("How many employees are in your business? : ")
                        # валидация ввода:
                        # если в employees не цифры, то до int(employees) выполнение не дойдет и ошибка не возникнет
                        if employees.isdigit() and 1 <= int(employees) <= 999999999999:
                            employees = int(employees)
                            print("Profit per employee is", f"{fin_result / employees:.2f}")
                            break

                        # конец валидации ввода employees
                        else:
                            print('Unreal employees number. Retype')
                            continue

                elif fin_result < 0:
                    print("Bad job, your business losses ", fin_result)

                else:
                    print("Break-even only. But zero profit is better than losses!")

                break

            # конец валидации ввода cost
            else:
                print('Unreal cost. Retype')
                continue
        break

    # конец валидации ввода revenue
    else:
        print('Unreal revenue. Retype')
        continue
