vblrychka = int(input('Введите значение выручки: '))
izderjki = int(input('Введите значение издержек:'))

if vblrychka > izderjki:
    print('У вас прибыль!')
    rent = (vblrychka - izderjki) / vblrychka
    print('Ваша рентабельность = ', rent)
    sotrydniki = int(input('Введите количество сотрудников: '))
    rent_na_sotrydnika = vblrychka / sotrydniki
    print(rent_na_sotrydnika)
else: print('У вас убытки =(')