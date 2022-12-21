def Input_value(msg1, msg2):
    while True:
        try:
            user_number = int(input(msg1))
            break
        except ValueError:
            print(msg2)
    return user_number


def To_bin(user_num):
    result = ''
    while True:
        if user_num % 2:
            result += '1'
        else:
            result += '0'
        user_num = user_num//2
        if user_num == 0:
            break
    return result[::-1]


user_number = Input_value('Введите целое цисло:  ', 'Введите целое цисло')
print(f'{user_number} -> {To_bin(user_number)}')
