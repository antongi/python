def division():
    var_1 = float(input('Введите первое число - '))
    var_2 = float(input('Введите второе число - '))
    try:
        result = var_1 / var_2
    except ZeroDivisionError:
        print('Делить на ноль нельзя!')
        return
    return result

a = division()

print(a)