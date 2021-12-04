print('Введите ваше имя: ')
el_0 = input()
print('Введите ваш возраст: ')
el_1= int(input())
print('Введите ваш рост в формате мм.сс: ')
el_2 = float(input())
print('Введите имя вашего питомца: ')
el_3 = input()
spisok = [el_0, el_1, el_2, el_3]

el_0, el_1 = el_1, el_0
el_2, el_3 = el_3, el_2
spisok = [el_0, el_1, el_2, el_3]
print(spisok)

