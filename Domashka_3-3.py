min_0 = None


def my_func():
    num_1 = int(input('Введите первое целое число - '))
    num_2 = int(input('Введите второе целое число - '))
    num_3 = int(input('Введите третье целое число - '))
    global min_0
    min_0 = min(num_1, num_2, num_3)
    if min_0 == num_1:
        print(num_2 + num_3)
    elif min_0 == num_2:
        print(num_1 + num_3)
    else:
        print(num_1 + num_2)


my_func()
