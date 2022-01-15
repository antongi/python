"""Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
число». Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте
работу проекта. Для этого создаёте экземпляры класса (комплексные числа), выполните
сложение и умножение созданных экземпляров. Проверьте корректность полученного
результата."""

class Complex_num:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def comp_real(self):
        return complex(self.a, self.b)

    def __str__(self):
        return f'({self.a}+{self.b}j)'

    def __add__(self, other):
        return Complex_num(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return Complex_num(self.a * other.a - self.b * other.b, self.b * other.a + self.a * other.b )


comp_1 = Complex_num(4, 5)
comp_2 = Complex_num(3, 4)

print(complex(4, 5) * complex(3, 4))
print(comp_1 * comp_2)

