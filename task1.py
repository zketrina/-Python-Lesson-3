#Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def dif(num_1,num_2):
    try:
        num_1 = int(num_1)
        num_2 = int(num_2)
    except ValueError:
        return "Value error"
    except ZeroDivisionError:
        return "Wrong devider! You can't use zero as a devider"
    dif_1 = num_1 / num_2
    return dif_1

print(dif(input("Введите число:"),input("Введите число:")))