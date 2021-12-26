class Car:
    def __init__(self, speed, color, name, is_police: bool):
        self.direction = None
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} начала движение!')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        self.direction = direction
        print(f'{self.name} повернула {self.direction}')
        
    def show_speed(self):
        print(f'{self.name} движется со скоростью {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        Car.show_speed(self)
        print('Куда гонишь, брат?') if self.speed > 60 else None


class SportCar(Car):
    def show_speed(self):
        Car.show_speed(self)


class WorkCar(Car):
    def show_speed(self):
        Car.show_speed(self)
        print('Куда гонишь, брат?') if self.speed > 40 else None


class PoliceCar(Car):
    def show_stat_police(self):
        print('FLag the Police!') if self.is_police is True else None


zaz = TownCar(70, 'Yellow', 'Zaz', False)  # Создание экземпляра класса
uaz = PoliceCar(150, 'Gray', 'Bobik', True)
zaz.show_speed()
zaz.turn('Налево')
print(zaz.color)
uaz.show_stat_police()

