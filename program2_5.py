print('Lesson 2_5 Рейтинг')

my_list = [7, 5, 3, 3, 2]


while True:

    print(my_list)
    rating = input('Input new rating or q for exit: ')

    if rating == 'q':
        break
    else:
        rating=int(rating)

    my_list.append(rating)
    my_list.sort(reverse=True)
