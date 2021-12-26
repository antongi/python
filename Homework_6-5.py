class Stationery():

    def __init__(self, title='Something'):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):

    def draw(self):
        print(f'Погнали рисовать {self.title}')


class Pencil(Stationery):

    def draw(self):
        print(f'Рисуем {self.title}')


class Handle(Stationery):

    def draw(self):
        print(f'Малюем {self.title}')


pen = Pen('Ручка')
pencil = Pencil('Крандаш')
handle = Handle('Маркер')

pen.draw()
pencil.draw()
handle.draw()

