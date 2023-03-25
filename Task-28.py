# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
# 4

def sum(a, b):
    if a == b == 0:
        return 0
    if a == b:
        return sum(a - 1, b - 1) + 2
    elif a > b:
        return sum(a - 1, b) + 1
    else:
        return sum(a, b - 1) + 1

a = int(input('Введите число A: '))
b = int(input('Введите число B: '))

print(f'Сумма чисел {a} и {b} равняется {sum(a, b)}.') 