def Input_value(msg1, msg2):
    while True:
        try:
            user_number = int(input(msg1))
            break
        except ValueError:
            print(msg2)
    return user_number


def Fibonachi(user_num):
    fib_list = [0, 1]
    for i in range(user_num-1):
        fib_list.append(fib_list[i]+fib_list[i+1])
    return fib_list


def Neg_fibonachi(user_num):
    fib_list = [0, 1]
    for i in range(user_num-1):
        fib_list.append(fib_list[i]-fib_list[i+1])
    return fib_list[::-1]


user_number = Input_value('Введите целое цисло:  ', 'Введите целое цисло')
result = Neg_fibonachi(user_number)+Fibonachi(user_number)[1:]
print(f'k={user_number} список чисел Фибоначчи {result}')
