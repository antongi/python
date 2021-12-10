my_list = []
line_list = []
n = 0
with open('Work-3.txt', encoding='utf-8', mode='r') as f:
    for line in f:
        line_list = (line.rstrip('\n')).split(' ')
        if float(line_list[1]) < 20000.00:
            print(f'Сотрудник {line_list[0]} - Малоимущий!!!')
        my_list.append(float(line_list[1]))
        n += 1
    print(f'Средняя зарплата сотрудников - {sum(my_list)/n:.2f}')
