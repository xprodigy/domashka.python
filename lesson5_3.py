print('Lesson 5_3:')

pay_all =[]
pay_20k = []

with open("people.txt", encoding="utf-8") as f_obj:
    print ('Сотрудники с окладом менее 20000:\n')
    for el in f_obj.readlines():
        i = el.split()
        if float(i[1]) < 20000:
            print (i[0])
            pay_20k.append(float(i[1]))
        pay_all.append(float(i[1]))

print ("\nСредний доход всех сотрудников:",round((sum(pay_all)/len(pay_all)),2))
print ("Средний доход низкооплачиваемых сотрудников:",round((sum(pay_20k)/len(pay_20k)),2))






