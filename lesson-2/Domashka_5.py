my_list = [7, 5, 3, 3, 2]
# my_list.insert(4, 3)
# print(int(my_list[1]))
new_el = int(input('Введите ваш рейтинг(натуральное число): '))
i = 0
print(my_list)
for el in my_list:
    if new_el <= el:
        i += 1

    elif new_el > el:
        break
# print(i)
my_list.insert(i, new_el)
print(my_list)




# my_list_1 = ' '.join(str(my_list))
# print(my_list_1)
# print('_'.join(['раз', 'два', 'три']))

# for el in my_list:
#     if el == new_el:
#         result = my_list.insert(my_list.index(el), new_el)
#         print(result)



