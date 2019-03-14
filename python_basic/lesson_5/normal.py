# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 05:20:48 2019
"""

# Задача-1

import easy
import os.path as osp
import os

loop = True
path = osp.dirname(__file__)
os.chdir(path)


while loop:
    print(" Работа с файловой системой ".center(79, "=") +
        f"\nТекущий каталог: {path}\n" +
        f"{'-'*79}\n" +
        "\t1 Перейти в каталог\n" +
        "\t2 Вывести содержимое текущего каталога\n" +
        "\t3 Удалить каталог\n" +
        "\t4 Создать каталог\n" +
        "\n\t0 Выход\n" +
        f"{'-'*79}\n")
    userInp = input("Введите пункт меню: ")
    if userInp.isdigit() and len(userInp) == 1:
        userInp = int(userInp)
    else:
        print("Ошибка! Введен некорректный пункт меню! Повторите ввод")
        continue
    if userInp == 0:
        loop = False
    elif userInp == 1:
        easy.subdirs(path)
        newpath = input("Введите каталог назначения: ")
        if osp.exists(newpath) and osp.isdir(newpath):
            path = osp.abspath(osp.join(path, newpath)) # abspath для поддержки перехода в родительский каталог по ".."
            os.chdir(path)
            print(f"...Выполнен переход в каталог {path}")
        else:
            print("Ошибка! Введен некорректный путь! Повторите ввод")
    elif userInp == 2:
        content = os.listdir(path)
        output = [('dir',d) for d in content if osp.isdir(osp.join(path, d))]
        output += [('file',f) for f in content if osp.isfile(osp.join(path, f))]
        if len(output) > 0:
            for tp, name in output:
                print(f"{tp}\t{name}")
        else:
            print("...Каталог пуст")
    elif userInp == 3:
        newpath = input("Введите путь к удаляемому каталогу: ")
        if osp.exists(newpath) and osp.isdir(newpath):
            os.remove(newpath)
            print("...Каталог удален")
        else:
            print("Ошибка! Введен некорректный путь! Повторите ввод")
    elif userInp == 4:
        dirname = input("Введите имя нового каталога: ")
        easy.create_dir(osp.join(path, dirname))

