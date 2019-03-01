# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 05:37:40 2019
"""

# Задание-1

print("\tВычисление координат")

equation = input("Введите выражение: ")
x = float(input("Введите координату x: "))

clear_equation = equation.replace(" ","").replace("y=","")
k, b = [float(i) for i in clear_equation.split('x')]

y = k * x + b

print(f"Ответ: y = {y:.2f}")

# ----------------------------------------------------------------------------

# Задание-2

print("\n\tПроверка корректности даты")

error = ""
inp_str = input("Введите дату в формате \"dd.mm.yyyy\": ")

days_in_month = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

d, m, y = inp_str.split(".")
if not (d.isdigit() and len(d) == 2 and int(d) > 0 and int(d) <= days_in_month[int(m)]):
    error += "День даты введен некорректно\n"
if not (m.isdigit() and len(m) == 2 and int(m) > 0 and int(m) <= 12):
    error += "Месяц даты введен некорректно\n"
if not (y.isdigit() and len(y) == 4 and int(y) > 0 and int(y) <= 9999):
    error += "Год даты введен некорректно\n"
if error:
    print(error)
else:
    print("Дата введена корректно")

# ----------------------------------------------------------------------------

# Задание-3

print("\n\tПеревёрнутая башня")

num_room = int(input("Введите номер комнаты: "))
cur_room = 0
floor = 0
room = 0
rooms_in_floor = 1

while cur_room != num_room:
    for f in range(1, rooms_in_floor + 1):          # этажи
        floor += 1
        room = 0
        for r in range(1, rooms_in_floor + 1):      # команты
            room = r
            cur_room += 1
            if cur_room == num_room:
                break
        if cur_room == num_room:
            break
    rooms_in_floor += 1

print(f"Выход: этаж {floor}, комната {room}")