"""Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите
параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
уникальные для каждого типа оргтехники."""


class Storage:
    pass


class OffEquip:

    def __init__(self, color: str, input_power: float, brand: str, weight: float):
        self.color = color
        self.input_power = input_power
        self.brand = brand
        self.weight = weight


class Printer(OffEquip):

    def __init__(self, color: str, input_power: float, brand: str, weight: float, print_speed: float, type_print: str):
        super().__init__(self, color, input_power, brand, weight)  # Почему он ругается и не видит weight???
        # self.weight = weight
        self.print_speed = print_speed
        self.type_print = type_print


class Scanner(OffEquip):

    def __init__(self, color: str, input_power: float, brand: str, weight: float, max_resolution_dpi: str,
                 deep_color_scan: str):
        super().__init__(color, input_power, brand, weight)
        self.max_resolution_dpi = max_resolution_dpi
        self.deep_color_scan = deep_color_scan


class Xerox(OffEquip):

    def __init__(self, color: str, input_power: float, brand: str, weight: float, speed_copy: str):
        super().__init__(color, input_power, brand, weight)
        self.speed_copy = speed_copy


scan = Scanner('Зеленый', 23.2, 'Canon', 14.5, '4800x4800', 'струйный')
printer = Printer('Зеленый', 23.2, 'Canon', 14.5, 4800, 'струйный')
