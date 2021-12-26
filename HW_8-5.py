"""Продолжить работу над четвертым(видимо) заданием. Разработать методы, отвечающие за приём оргтехники на склад и
передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а
также других данных, можно использовать любую подходящую структуру, например словарь."""


class Storage:

    my_list_stor = []
    @classmethod
    def add_stor(cls, location, amount):
        Storage.my_list_stor.extend((location.__name__, {cls.__name__: amount}))
        print(Storage.my_list_stor)


    @classmethod
    def move_in_subunit(cls, new_location, move_amount):
        my_list_subunit = []
        Storage.my_list_stor[0] = new_location
        Storage.my_list_stor[1][cls.__name__] = move_amount
        Storage.my_list_subunit.extend


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
Scanner.add_stor(Storage, 5)
