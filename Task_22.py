import random


def Gen_list(list_lens):
    user_list = []
    for i in range(list_lens):
        user_list.append(random.randint(-20, 20))
    return user_list


while True:
    try:
        user_number = int(input('Введите длинну массива:  '))
        break
    except ValueError:
        print('Введите целое цисло')
user_list=Gen_list(user_number)
sum=0
for i in range(1, len(user_list), 2):
    sum+=user_list[i]
print(f'{user_list} -> сумма эл-тов на нечетных индексах: {sum}')