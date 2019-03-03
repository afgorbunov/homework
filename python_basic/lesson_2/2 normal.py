# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 04:16:23 2019
"""

# Задача-1

from math import sqrt

print("\tВычисление квадратных корней")

inp_char = " "
i = 0
num_list = []

print("Введите список целых чисел:")
while inp_char != "":
    inp_char = input(f"\t{i:2d}:")
    if inp_char.isdigit():
        num_list.append(int(inp_char))
    i += 1

out_list = [int(sqrt(i)) for i in num_list if (i > 0) and (sqrt(i) % 1 == 0)]

print("Ответ:",out_list)

# ----------------------------------------------------------------------------

# Задача-2

print("\n\tПарсинг даты")

months = {
    1: "января",
    2: "февраля",
    3: "марта",
    4: "апреля",
    5: "мая",
    6: "июня",
    7: "июля",
    8: "августа",
    9: "сентября",
    10: "октября",
    11: "ноября",
    12: "декабря",
}

inp_str = input("Введите дату в формате \"dd.mm.yyyy\": ")
if inp_str != "" and int(inp_str[0:2]) <= 31 and int(inp_str[3:5]) <= 12:
    print(f"{inp_str[0:2]} {months[int(inp_str[3:5])]} {inp_str[-4:]} года")

# ----------------------------------------------------------------------------

# Задача-3

from random import randint

print("\n\tГенерация случайного списка")

len_list = int(input("Введите длинну генерируемого списка: "))
print([randint(-100, 100) for i in range(len_list)])

# ----------------------------------------------------------------------------

# Задача-4

print("\n\tПодсчет повторяющихся элементов списка")

inp_char = " "
i = 0
num_list = []

print("Введите список целых чисел:")
while inp_char != "":
    inp_char = input(f"\t{i:2d}:")
    if inp_char.isdigit():
        num_list.append(int(inp_char))
    i += 1

uniq = list(set(num_list))

print("Ответ 1:", uniq)
print("Ответ 2:", [i for i in uniq if num_list.count(i) == 1])
