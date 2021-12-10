my_list = []
char = ''
sum_n = []
char_i = []
char_l = []
my_f = open('Work-6.txt', encoding='UTF-8', mode='r')
for line in my_f:
    my_list.append(line.split(':'))  # Перебираем строки и создаем список из списков(наши строки)
for el_0 in my_list:
    for i in el_0[1]:  # При переборе общего списка, перебираем часть вложенного списка с числами.
        if i.isdigit():  # Если символ - числовой, пользуемся конкатенацией
            char = char + i
        elif i == '(':  # Если дошли до ( значит пора переводить получившуюся строку в int
            char_i.append(int(char))  # и добавляем в промежуточный список
            char = ''  # Очищаем вспомогательную переменную
    el_0[1] = sum(char_i)  # Для красоты)
    sum_n.append(sum(char_i))
    char_i.clear()
print(my_list)
for el_1 in my_list:  # Делаем отдельный список с ключами
    char_l.append(el_1[0])
print(char_l)
print(sum_n)
result_d = dict(zip(char_l, sum_n))  # Склеиваем списки в словарь
print(result_d)
my_f.close()