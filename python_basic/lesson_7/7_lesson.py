# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 05:29:06 2019
"""

import random
from sys import exit as s_exit

class LotoCell():
    def __init__(self):
        self.number = 0
        self.status = True

    def __str__(self):
        if self.status and self.number > 0:
            return str(self.number).rjust(2," ")
        elif self.number == 0:
            return "  "
        else:
            return "--"


class LotoString():
    def __init__(self):
        self.cells = [LotoCell() for i in range(9)]
        self.index_cells = []
        self.len = 0

    def generate(self, master_list):
        index_list = list(range(9))
        for i in range(5):
            ind = random.randint(0,len(index_list)-1)
            master_ind = random.randint(0,len(master_list)-1)
            self.cells[index_list[ind]].number = master_list[master_ind]
            del index_list[ind]
            del master_list[master_ind]

    def num_in(self, num):
        for c in self.cells:
            if c.number == num:
                return True
        return False

    def index(self, num):
        for c in range(len(self.cells)):
            if self.cells[c].number == num:
                return c
        return None

    def is_all_cross_out(self):
        res = True
        for c in self.cells:
            if c.number > 0 and c.status:
                res = False
        return res

    def __str__(self):
        return ' '.join([str(i) for i in self.cells])


class LotoCard():
    def __init__(self, player):
        self.player = player
        self.strings = [LotoString() for i in range(3)]
        self.border = '-'

    def generate(self):
        all_numbers_list = list(range(1,91))
        for s in self.strings:
            s.generate(all_numbers_list)
        print(f"Для игрока {self.player} создана карта")
        print(str(self))

    def num_in(self, num):
        for s in self.strings:
            if s.num_in(num):
                return True
        return False

    def index(self, num):
        for s in range(len(self.strings)):
            if self.strings[s].num_in(num):
                return s, self.strings[s].index(num)
        return None, None

    def cross_out(self, num):
        if self.num_in(num):
            s, c = self.index(num)
            self.strings[s].cells[c].status = False

    def is_all_cross_out(self):
        res = True
        for s in self.strings:
            if not s.is_all_cross_out():
                res = False
        return res

    def __str__(self):
        out = f"{self.border*2} {(self.player+' ').ljust(27,self.border)}\n"
        for s in self.strings:
            out += f"| {str(s)} |\n"
        out += f"{self.border*30}\n"
        return out


class LotoPlayer():
    def __init__(self, name, is_human=False):
        self.name = name
        self.card = LotoCard(self.name)
        self.card.generate()
        self.is_human = is_human


class LotoGame():
    def __init__(self, humans=1, computers=1):
        self.players = []
        self.turn = 0
        self.victory = False
        self.all_numbers = list(range(1,91))
        for h in range(humans):
            self.players.append(LotoPlayer(
                input(f"Игрок {h+1} > Введите свое имя: "),
                is_human=True,
            ))
        for c in range(computers):
            self.players.append(LotoPlayer(f"Компьютер {c+1}"))

    def humans_in(self):
        res = False
        for p in self.players:
            if p.is_human:
                res = True
        return res

    def run(self):
        while not self.victory:
            self.turn += 1
            print(f" Ход {self.turn} ".center(79, "="))
            ind = random.randint(0,len(self.all_numbers)-1)
            num = self.all_numbers[ind]
            del self.all_numbers[ind]
            print(f" Выпал номер {num} ".center(79, ' ')+'\n')
            for p in self.players:
                print(p.card)
                if p.is_human:
                    answ = input(f"{p.name} > Зачеркнуть данное число? (д/н): ")
                    if answ.lower() in ["д", "да", "y", "yes", "1", "true"]:
                        if p.card.num_in(num):
                            p.card.cross_out(num)
                            print(f"{p.name} > Вычеркнуто число {num}")
                            if p.card.is_all_cross_out():
                                self.victory = True
                                if self.turn == 15:
                                    print(f"{p.name} > Поздравляем! Вы выиграли ДЖЕК-ПОТ на {turn} ходу!!!")
                                else:
                                    print(f"{p.name} > Поздравляем! Вы выиграли на {self.turn} ходу!!!")
                        else:
                            print(f"{p.name} > Данного числа нет в Вашей карте. К сожалению, Вы проиграли.")
                            print(f"Игрок {p.name} выбывает из игры.")
                            del self.players[self.players.index(p)]
                    elif answ.lower() in ["н", "нет", "n", "no", "0", "false", ""]:
                        if p.card.num_in(num):
                            print(f"{p.name} > Данное число есть в Вашей карте. К сожалению, Вы проиграли.")
                            del self.players[self.players.index(p)]
                else:
                    if p.card.num_in(num):
                        p.card.cross_out(num)
                        print(f"{p.name} > Вычеркнуто число {num}")
                        if p.card.is_all_cross_out():
                            self.victory = True
                            if turn == 15:
                                print(f"{p.name} > Поздравляем! Вы выиграли ДЖЕК-ПОТ на {turn} ходу!!!")
                            else:
                                print(f"{p.name} > Поздравляем! Вы выиграли на {turn} ходу!!!")
            if not self.humans_in():
                print("Игра окончена в связи с тем, что все игроки-люди выбыли!")
                self.victory = True

if __name__ == "__main__":
    print("="*79)
    print(" Игра Лото ".center(79,'+'))
    print("="*79, '\n')
    hum = input("Введите количество игроков-людей: ")
    if hum.isdigit():
        hum = int(hum)
    else:
        print("\tОшибка! Введено некорректное значение! ")
        s_exit(0)
    comp = input("Введите количество игроков-компьютеров: ")
    if comp.isdigit():
        comp = int(comp)
    else:
        print("\tОшибка! Введено некорректное значение! ")
        s_exit(0)
    game = LotoGame(humans=hum, computers=comp)
    game.run()

