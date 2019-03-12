# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 04:23:19 2019
"""

def input_arr(invitation, num=False):
    arr = []
    inp = " "
    print(invitation)
    while inp != "":
        inp = input(f"\t{len(arr)}: ")
        if inp != "":
            if num and inp.isdigit():
                inp = int(inp)
            arr.append(inp)
    return arr

# ----------------------------------------------------------------------------

# Задание-1

print("\tВозведение списка в квадрат")

arr = input_arr("Введите список целых чисел", num=True)

print("Ответ:", [i**2 for i in arr])
print("-"*70)

# ----------------------------------------------------------------------------

# Задание-2

print("\tСовпадение списков")

arr1 = input_arr("Введите список фруктов 1")
arr2 = input_arr("Введите список фруктов 2")

print("Ответ:", [i for i in arr1 if i in arr2])
print("-"*70)

# ----------------------------------------------------------------------------

# Задание-3

print("\tСелективная генерация списка")

arr = input_arr("Введите список целых чисел", num=True)

print("Ответ:", [i for i in arr if (i > 0) and (i % 3 == 0) and (i % 4 != 0)])
