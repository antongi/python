class Cell:

    def __init__(self, box):
        self.box = box

    def __add__(self, other):
        return self.box + other.box

    def __sub__(self, other):
        if self.box - other.box > 0:
            return self.box - other.box
        else:
            return f'Разность количества ячеек меньше или равна нулю!'

    def __mul__(self, other):
        return self.box * other.box

    def __truediv__(self, other):
        return self.box // other.box

    def make_order(self):
        for el in range(1, self.box + 1):
            if el % 5 == 0:
                print('*\n')
            else:
                print('*', end='')


cell_1 = Cell(17)
cell_2 = Cell(6)
print(cell_1 - cell_2)
print(cell_1 + cell_2)
print(cell_1 / cell_2)
print(cell_1 * cell_2)
cell_1.make_order()