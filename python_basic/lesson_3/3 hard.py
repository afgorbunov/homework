# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 15:13:06 2019
"""


def attack(assaulter, defender):
    damage = damagekWithArmor(assaulter, defender)
    defender["health"] -= damage
    print(f'{assaulter["name"]} наносит {defender["name"]} {damage:.2f} единиц урона')


def damagekWithArmor(assaulter, defender):
    return assaulter["damage"] / defender["armor"]


def runGame(*args):
    wariorsFiles = [open(w, "r", encoding="utf-8") for w in args]
    wariors = []
    for wf in wariorsFiles:
        wariors.append({par: (float(val) if val.replace(".","").isdigit() else val) for par, val in [l.replace("\n", "").split("=") for l in wf.readlines()]})
        wf.close()

    victory = False

    while not victory:
        for w in wariors:
            restWariors = [i for i in wariors if w != i]
            for r in restWariors:
                attack(w, r)
                if r["health"] <= 0:
                    victory = True
                    print(f'{w["name"]} победил! Осталось {w["health"]:.2f} жизней!')
                    break
            if victory:
                break


if __name__ == '__main__':
    print("\tИгра")
    player = {
        "name": input("Введите имя игрока: "),
        "health": 100,
        "damage": 70,
        "armor": 1.2,
    }
    enemy = {
        "name": input("Введите имя врага: "),
        "health": 200,
        "damage": 50,
        "armor": 0.9,
    }

    with open(player["name"] + ".txt", "w", encoding="utf-8") as f:
        f.write("\n".join([f"{n}={s}" for n, s in player.items()]))
    with open(enemy["name"] + ".txt", "w", encoding="utf-8") as f:
        f.write("\n".join([f"{n}={s}" for n, s in enemy.items()]))

    runGame(player["name"] + ".txt", enemy["name"] + ".txt")