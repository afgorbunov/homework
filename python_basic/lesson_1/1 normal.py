# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 05:08:57 2019
"""

print("\tВозведение в степень")

num = int(input("Введите число: "))

while not (num >= 0 and num <= 10):
    print("Введено неверное число! Число должно быть в диапазоне 0 <= x <= 10")
    num = int(input("Введите число еще раз: "))

print("Число", num, "в квадрате равно", num**2)

# --------------

print("\n\tОбмен переменных")
print("Введите ниже два любых числа")

x = int(input("x = "))
y = int(input("y = "))

x = x + y
y = x - y
x = x - y

print("Произведен обмен значений переменными")
print("x =", x)
print("y =", y)
