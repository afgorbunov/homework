# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 04:56:08 2019
"""

# Задание - 1

print("\tУпаковка данных")

def packData(name, age, city):
    return f"{name.title()}, {age:d} год(а), проживает в городе {city.title()}"

user_name = input("Введите имя: ")
user_age = int(input("Введите возраст: "))
user_city = input("Введите название города: ")
print("Ответ:", packData(user_name, user_age, user_city))
print("-"*70)

# ----------------------------------------------------------------------------

# Задание - 2

print("\n\tПоиск максимального значения")


def maxNum(x, y, z):
    my_max = x if x > y else y
    return my_max if my_max > z else z


print("Введите целые числа")
nums = []
for i in range(1, 4):
    nums.append(int(input(f"\t{i:d}:")))

print("Максимальное число из введенных:", maxNum(*nums))
print("-"*70)

# ----------------------------------------------------------------------------

# Задание - 3

print("\n\tПоиск длинной строки")


def maxStringLen(*args):
    len_list = list(map(len, args))
    return args[len_list.index(max(len_list))]


print("Введите строки (пустая строка для окончания ввода)")
inp = " "
inp_list = []
count = 1

while inp != "":
    inp = input(f"\t{count:d}: ")
    if inp != "":
        inp_list.append(inp)
    count += 1

print(f"Строка с наибольшей длинной: \"{maxStringLen(*inp_list)}\"")
