from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def calc(self):
        pass

    def __add__(self, other):
        return self.calc + other.calc


class Coat(Clothes):

    @property
    def calc(self):
        return self.param / 6.5 + 0.5


class Suit(Clothes):

    @property
    def calc(self):
        return 2 * self.param + 0.3


palto = Coat(6.5)
print(palto.calc)
costume = Suit(4)
print(costume.calc)
print(palto + costume)