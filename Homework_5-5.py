from random import randrange
list_rm = [randrange(10, 50) for i in range(10)]
print(f'Ваши числа - {list_rm}\nИщите их в файле Work-5.txt\nСумма ваших чисел - {sum(list_rm)}')
my_f_w = open('Work-5.txt', 'w')
my_f_w.write(' '.join(str(el) for el in list_rm))
my_f_w.close()