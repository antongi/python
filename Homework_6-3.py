class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': 25000, 'bonus': 5000}


class Position(Worker):
    def get_full_name(self):
        return self.surname + ' ' + self.name  # print(f'Полное имя сотрудника: {self.surname} {self.name}.')

    def get_total_income(self):
        total_income = self._income.get('wage') + self._income.get('bonus')
        print(f'Доход сотрудника {self.name} - {total_income}.')


rab = Position('Вася', 'Пупкин', 'Раб')
print(rab.get_full_name())
rab.get_total_income()
print(f'Сотрудник {rab.get_full_name()} работает на позиции: {rab.position}')
