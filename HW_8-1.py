"""Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
Он должен извлекать число, месяц, год и преобразовывать их тип
к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
реальных данных.
"""
class Date:

    def __init__(self, date: str):
        self.date = date

    @classmethod
    def int_method(cls, param):
        return list(map(int, param.split('-')))

    @staticmethod
    def valid_method(param):
        l_d = list(map(int, param.split('-')))
        if l_d[0] > 32 or l_d[0] < 1 or l_d[1] < 0 or l_d[1] > 12 or l_d[2] < 1 or l_d[2] > 2099:
            print('Date invalid')
        else:
            print('Date valid')


dt = Date('10-12-2021')
print(Date.int_method('10-12-2021'))
print(dt.int_method(dt.date))
Date.valid_method('01-12-2099')
Date.valid_method('00-13-2100')


