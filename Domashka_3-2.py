def user(name:str, surname:str, year_of_birth:int, city:str, mail:str, telephone:int):
    print(f'Имя - {name}; Фамилия - {surname}; Год рождения - {year_of_birth}; Город проживания - {city}; '
          f'Email - {mail}; Номер телефона - {telephone}')


user(name=input('Введите ваше имя - '), surname=input('Введите вашу фамилию - '),
     year_of_birth=int(input('Введите год рождения - ')), city=input('Введите город проживания - '),
     mail=input('Введите ваш email - '), telephone=int(input('Введите ваш номер телефона - ')))
