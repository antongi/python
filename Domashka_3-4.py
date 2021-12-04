# def my_func(x: float, y: int):
#     result = x ** y
#     print(result)
#
#
# my_func(2, -3)


def my_func(x: float, y: int):
    z = x
    while abs(y) - 1 != 0:
        z = z * x
        y += 1
        print(z)
    result = 1 / z
    print(result)


my_func(3, -4)