print('Lesson 5_7')

import json

average_profit = []
dictionary = {}

with open("firms.txt", encoding="utf-8") as f_obj:
    for el in f_obj.readlines():
        i = el.split()
        if int(i[2])-int(i[3]) >= 0:
            average_profit.append(int(i[2])-int(i[3]))
        dictionary.update({i[0]: int(i[2])-int(i[3])})
result_list = [ dictionary, {"average_profit": round((sum(average_profit)/len(average_profit)),2) }]

print(result_list)

with open("my_file.json", "w") as write_f:
    json.dump(result_list, write_f)
