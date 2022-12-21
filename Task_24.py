import random


def Gen_list(list_lens):
    user_list = []
    for i in range(list_lens):
        user_list.append(round(random.uniform(-20, 20), 2))
    return user_list


def Input_value(msg1, msg2):
    while True:
        try:
            user_number = int(input(msg1))
            break
        except ValueError:
            print(msg2)
    return user_number


def Take_fract_part(user_list):
    work_list = []
    for i in user_list:
        my_str = str(i)
        my_str = my_str[my_str.find('.')+1:]
        if len(my_str) == 1:
            my_str = int(my_str)*10
        else:
            my_str = int(my_str)
        work_list.append(my_str)
    return work_list


user_number = Input_value('Введите длинну массива:  ', 'Введите целое цисло')
user_list = Gen_list(user_number)
work_list = Take_fract_part(user_list)
diff=(max(work_list)-min(work_list))/100
print(f'{user_list} => {diff}')
