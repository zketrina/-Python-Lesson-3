# Реализовать функцию my_func(),
# которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
def my_func (num_1,num_2,num_3):
    num_1 = int(num_1)
    num_2 = int(num_2)
    num_3 = int(num_3)
    return sum(sorted([num_1,num_2,num_3])[1:])
print(my_func(input("Введите число:"),input("Введите число:"),input("Введите число:")))





