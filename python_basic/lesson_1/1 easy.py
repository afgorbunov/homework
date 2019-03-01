# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 04:45:28 2019
"""

outstring = "\tПрограмма приветствия"
print(outstring)

name = input("Введите Ваше имя: ")
print("Добрый день,", name)

# --------------

num = input("Введите любое число от 0 до 10: ")
print(num, "+ 2 =", int(num) + 2)

# --------------

age = int(input("Введите Ваш возраст: "))
if age >= 18:
    print("Доступ разрешен")
else:
    print("Извините, пользование данным ресурсом разрешено только с 18 лет")
