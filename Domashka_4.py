num_user = int(input('Введите целое положительное число: '))  # Запрашиваем писло

num_ostatok_1 = num_user % 10  # Сразу отделяем младший разряд путем нахождения остатка от деления
num_user = num_user // 10  # Оставшиеся числа
# print(num_user, num_ostatok_1)

while num_user > 0:  # Условие в цикле для проверки всех чисел
    num_ostatok_2 = num_user % 10  # Получаем следующее число
    if num_ostatok_2 > num_ostatok_1:  # Сравниваем и если следующее число больше замещаем
        num_ostatok_1 = num_ostatok_2  # "Должен остаться только один!"
        # print(num_user, num_ostatok_1)

    num_user = num_user // 10  # Отделяем для перехода на следующую итерацию

print(num_ostatok_1)
