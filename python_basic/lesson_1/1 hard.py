# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 05:25:45 2019
"""

print("\tМедицинская анкета")
print("Введите ваши данные")
name = input("\tимя: ")
family = input("\tфамилия: ")
age = int(input("\tвозраст: "))
weight = int(input("\tмасса тела: "))
print("-"*78)

if (age >= 0 and age < 30) and (weight >= 50 and weight < 120):
    conclusion = "состояние хорошее"
elif (age >= 30 and age < 40) and (weight < 50 or weight >= 120):
    conclusion = "необходимо вести здоровый образ жизни"
elif age >= 40 and (weight < 50 or weight >= 120):
    conclusion = "необходимо срочно обратиться к врачу"
else:
    conclusion = "состояние вполне приемлемо"

print("Заключение:\n\t{} {}, лет {}, масса тела {} кг - {}".format(
    family.title(),
    name.title(),
    age,
    weight,
    conclusion,
))
