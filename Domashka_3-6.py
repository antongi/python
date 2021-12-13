def int_func(word):
    return word.title()


usr_inp = input('Введите строку из английских слов - ').split(' ')
for el in range(len(usr_inp)):
    usr_inp[el] = int_func(usr_inp[el])
usr_inp = ' '.join(usr_inp)
print(usr_inp)