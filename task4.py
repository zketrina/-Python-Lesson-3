# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
def my_func (x, y):
    x = int(x)
    y = int(y)
    num = 1 / x ** abs(y)
    return num
print(my_func(input("Введите положительное число:"),input("Введите целое отрицательное число:")))





