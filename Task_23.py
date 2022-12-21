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
user_list = Gen_list(user_number)
i = 0
result = []
while True:
    if i <= len(user_list)-1-i:
        result.append(user_list[i]*user_list[len(user_list)-i-1])
        i += 1
    else:
        break
print(f'{user_list} => {result}')
