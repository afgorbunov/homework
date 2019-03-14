# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 05:09:28 2019
"""

# Задача - 1


class Person():
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def attack(self, defender):
        sum_damage = self._damagekWithArmor(defender)
        defender.health -= sum_damage
        print(f'{self.name} наносит {defender.name} {sum_damage:.2f} единиц урона')

    def _damagekWithArmor(self, defender):
        return self.damage / defender.armor


class Player(Person):
    def __init__(self, health, damage, armor):
        name = input("Введите имя игрока: ")
        super(Player, self).__init__(name, health, damage, armor)


class Enemy(Person):
    def __init__(self, health, damage, armor):
        name = input(f"Введите имя врага: ")
        super(Enemy, self).__init__(name, health, damage, armor)


class Game():
    def __init__(self):
        self.player = Player(100, 70, 1.6)
        self.enemy = Enemy(200, 30, 0.4)
        self.victory = False
        self._wariors = self.player, self.enemy

    def run(self):
        while not self.victory:
            for w in self._wariors:
                restWariors = [i for i in self._wariors if w != i]
                for r in restWariors:
                    w.attack(r)
                    if r.health <= 0:
                        self.victory = True
                        print(f'{w.name} победил! Осталось {w.health:.2f} жизней!')
                        break
                if self.victory:
                    break


if __name__ == '__main__':
    game = Game()
    game.run()