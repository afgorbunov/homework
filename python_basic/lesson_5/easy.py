# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 04:12:50 2019
"""

import os
import os.path as osp
import shutil

# Задача-1


def create_dir(path):

        newpath = osp.normpath(path)
        if not osp.exists(newpath):
            os.mkdir(newpath)
            print(f"Создан каталог: {newpath}")
        else:
            print(f"Каталог {newpath} уже существует")

# ----------------------------------------------------------------------------

# Задача-2

def subdirs(path):
    dirs = [f for f in os.listdir(path) if osp.isdir(f)]

    if len(dirs) > 0:
        print(f"В каталоге \"{path}\" существует {len(dirs)} подкаталогов:")
        for d in dirs:
            print(f"\t{d}")
    else:
        print(f"В каталоге \"{path}\" нет подкаталогов.")

# ----------------------------------------------------------------------------

# Задача-3

def copy_file(path, new_file_name):
    shutil.copy2(path, osp.join(osp.dirname(path),new_file_name))
    print(f"В каталоге \"{osp.dirname(path)}\" создана копия файла "+
          f"\"{osp.basename(path)}\" с названием \"{new_file_name}\"")

# ----------------------------------------------------------------------------

# Запуск

if __name__ == '__main__':
    print("\tСоздание каталогов")
    for i in range(1,10):
        create_dir(osp.join(osp.dirname(__file__),"dir_" + str(i)))
    print("-" * 70)

    print("\tВывод каталогов")
    subdirs(osp.dirname(__file__))
    print("-" * 70)

    print("\tКопирование файла")
    copy_file(__file__, "copies_" + osp.basename(__file__))