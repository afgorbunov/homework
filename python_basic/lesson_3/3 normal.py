# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 07:20:55 2019
"""

names = ['Вася', 'Коля', 'Дима', 'Саша', 'Рома', 'Леша']
salary = [20000, 30000, 15000, 460000, 1340000, 845000]

salary_dict = {n: s for n, s in zip(names, salary) if s < 500000}

with open('salary.txt', 'w', encoding="utf-8") as f:
    for n, s in salary_dict.items():
        f.write(f"{n} - {s:d}\n")

with open('salary.txt', 'r', encoding="utf-8") as f:
    for line in f.readlines():
        n, s = line.replace('\n', '').split(" - ")
        print(f"{n.upper()} - {int(s)-int(s)*0.13:.2f}")
