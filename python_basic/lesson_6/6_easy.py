# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 12:08:50 2019
"""

# Задача - 1, 2


class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Автомобиль {self.name} поехал")

    def stop(self):
        print(f"Автомобиль {self.name} остановился")

    def turn(self, direction):
        if direction != "налево" and direction != "направо":
            print("Указано неверное направление")
            return
        print(f"Автомобиль {self.name} повернул {direction}")

    def __str__(self):
        return f"{self.color} {self.name}"


class TownCar(Car):
    def __init__(self, speed, color, name):
        super(TownCar, self).__init__(speed, color, name, False)


class SportCar(Car):
    def __init__(self, speed, color, name):
        super(SportCar, self).__init__(speed, color, name, False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super(WorkCar, self).__init__(speed, color, name, False)


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super(PoliceCar, self).__init__(speed, color, name, True)
