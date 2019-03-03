# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 08:21:34 2019
"""

# Задача-1

print("\tФорматированный вывод фруктов")

fruits = ["яблоко", "банан", "киви", "арбуз"]
len_fruits = [len(f) for f in fruits]
max_len = max(len_fruits)

for f in range(len(fruits)):
    print(f"{f+1}. {fruits[f].rjust(max_len,' ')}")

# -----------------------------------------------------------------------------

# Задача-2

print("\n\tВычитание списков")

inp_char = " "
i = 0
first_list = []
second_list = []

print("Введите первый список:")
while inp_char != "":
    inp_char = input(f"\t{i:2d}:")
    if inp_char != "":
        first_list.append(inp_char)
    i += 1

inp_char = " "
i = 0
print("Введите второй список:")
while inp_char != "":
    inp_char = input(f"\t{i:2d}:")
    if inp_char != "":
        second_list.append(inp_char)
    i += 1

print("Ответ:",[i for i in first_list if not i in second_list])

# -----------------------------------------------------------------------------

# Задача-3:

print("\n\tВычитание списков")

inp_char = " "
i = 0
num_list = []

print("Введите список целых чисел:")
while inp_char != "":
    inp_char = input(f"\t{i:2d}:")
    if inp_char.isdigit():
        num_list.append(int(inp_char))
    i += 1

out_list = []
for i in num_list:
    if i % 2 == 0:
        out_list.append(i/4)
    else:
        out_list.append(i*2)

print("Ответ:",out_list)