def my_func():
    sum_0 = 0
    while True:
        list_0 = input('Введите чисела, для выхода введите q - ').split(' ')
        for el in list_0:
            if el == 'q':
                list_1 = list_0[:list_0.index('q')]
                result_0 = [int(elem) for elem in list_1]
                print(result_0)
                sum_0 = sum(result_0) + sum_0
                print(sum_0)
                return
        result_0 = [int(elem) for elem in list_0]
        print(result_0)
        sum_0 = sum(result_0) + sum_0
        print(sum_0)


my_func()