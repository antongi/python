class Road:
    def __init__(self, length, width):
        self.mass = None
        self.depth = None
        self._length = length
        self._width = width

    def calc_asphalt(self, dept, mass=25):
        self.mass = mass
        self.depth = dept
        print(f'{int((self._length * self._width * self.mass * self.depth) / 1000)} т')
        """ масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см - по идее это постоянная
        величина, значит можно не передавать ничего и подставить 25 в формулу вместо self.mass """


mass_road = Road(20, 5000)
mass_road.calc_asphalt(5)




