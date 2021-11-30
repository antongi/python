# season = list('Зима Весна Лето Осень')
# print('Введите номер месяца от 1 до 12: ')
# user_month = int(input())
#
# if user_month == 12 or user_month == 1 or user_month == 2:
#     print(''.join(season[:4]))
# elif user_month == 3 or user_month == 4 or user_month == 5:
#     print(''.join(season[5:10]))
# elif user_month == 6 or user_month == 7 or user_month == 8:
#     print(''.join(season[11:15]))
# elif user_month == 9 or user_month == 10 or user_month == 11:
#     print(''.join(season[16:21]))


season = dict(winter='Зима', spring='Весна', summer='Лето', autumn='Осень')
print('Введите номер месяца от 1 до 12: ')
user_month = int(input())

if user_month == 12 or user_month == 1 or user_month == 2:
    print(season['winter'])
elif user_month == 3 or user_month == 4 or user_month == 5:
    print(season['spring'])
elif user_month == 6 or user_month == 7 or user_month == 8:
    print(season['summer'])
elif user_month == 9 or user_month == 10 or user_month == 11:
    print(season['autumn'])

