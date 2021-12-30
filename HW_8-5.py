"""Продолжить работу над четвертым(видимо) заданием. Разработать методы, отвечающие за приём оргтехники на склад и
передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а
также других данных, можно использовать любую подходящую структуру, например словарь."""
# my_list_stor = {}
# my_list_office = {}
# my_list_tech = {}

class Storage:

    my_list_stor = {}
    my_list_office = {}
    my_list_tech = {}

    @classmethod
    def add_stor(cls, amount):
        Storage.my_list_stor[cls.__name__] = amount
        print(f'Поступило на склад: {Storage.my_list_stor}')

    @classmethod
    def move_in_subunit(cls, new_location, move_amount):
        if new_location == 'office' and Storage.my_list_stor[cls.__name__] != 0:
            if Storage.my_list_stor[cls.__name__] >= move_amount:
                Storage.my_list_office[cls.__name__] = move_amount
                Storage.my_list_stor[cls.__name__] = Storage.my_list_stor[cls.__name__] - move_amount
                print(f'Перемещено в офис: {Storage.my_list_office}. Остаток на складе: {Storage.my_list_stor}')
            elif Storage.my_list_stor[cls.__name__] < move_amount:
                differ_move = move_amount - Storage.my_list_stor[cls.__name__]
                Storage.my_list_office[cls.__name__] = Storage.my_list_stor[cls.__name__]
                Storage.my_list_stor[cls.__name__] = 0
                print(f'Перемещено в офис: {Storage.my_list_office}. Остаток на складе: {Storage.my_list_stor}'
                      f'Необходимо докупить единиц перемещаемой техники - {differ_move}')
        elif new_location == 'tech' and Storage.my_list_stor[cls.__name__] != 0:
            if Storage.my_list_stor[cls.__name__] >= move_amount:
                Storage.my_list_tech[cls.__name__] = move_amount
                Storage.my_list_stor[cls.__name__] = Storage.my_list_stor[cls.__name__] - move_amount
                print(f'Перемещено в офис: {Storage.my_list_tech}. Остаток на складе: {Storage.my_list_stor}')
            elif Storage.my_list_stor[cls.__name__] < move_amount:
                differ_move = move_amount - Storage.my_list_stor[cls.__name__]
                Storage.my_list_tech[cls.__name__] = Storage.my_list_stor[cls.__name__]
                Storage.my_list_stor[cls.__name__] = 0
                print(f'Перемещено в тех.отдел: {Storage.my_list_tech}. Остаток на складе: {Storage.my_list_stor}'
                      f'Необходимо докупить единиц перемещаемой техники - {differ_move}')
        else:
            print('Введено некорректное наименование подразделения! Попробуйте еще.')


class OffEquip(Storage):

    def __init__(self, color, input_power, brand, weight):
        self.color = color
        self.input_power = input_power
        self.brand = brand
        self.weight = weight


class Printer(OffEquip):

    def __init__(self, color, input_power, brand, weight, print_speed, type_print):
        super().__init__(self, color, input_power, brand)
        self.weight = weight
        self.print_speed = print_speed
        self.type_print = type_print


class Scanner(OffEquip):

    def __init__(self, color, input_power, brand, weight, max_resolution_dpi, deep_color_scan):
        super().__init__(color, input_power, brand, weight)
        self.max_resolution_dpi = max_resolution_dpi
        self.deep_color_scan = deep_color_scan


class Xerox(OffEquip):

    def __init__(self, color, input_power, brand, weight, speed_copy):
        super().__init__(color, input_power, brand, weight)
        self.speed_copy = speed_copy


scan = Scanner('Зеленый', 23.2, 'Canon', 14.5, '4800x4800', 'струйный')
printer = Printer('Зеленый', 23.2, 'Canon', 14.5, 4800, 'струйный')
scan.add_stor(5)
scan.move_in_subunit('office', 4)
