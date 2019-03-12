# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 05:01:09 2019
"""

import re

# Задача - 1

print("\tПроверка корректности почты")

def match_string(var, pattern, string):
    res = re.match(pattern, string)
    return_str = f'Значение переменной \"{var}\" введен '
    if res:
        return return_str + 'корректно'
    else:
        return return_str + 'не корректно'

name = input("Введите имя: ")
family = input("Введите фамилию: ")
email = input("Введите e-mail: ")

print(match_string('Имя', r'[A-ZА-Я]\w+', name))
print(match_string('Фамилия', r'[A-ZА-Я]\w+', family))
print(match_string('e-mail', r"[\w\d_]+@[\w\d]+\.(ru|com|org)", email))
print("-"*70)

# ----------------------------------------------------------------------------

# Задача - 2

print("\n\tПоиск многоточий")

some_str = '''
Мороз и солнце; день чудесный!
Еще ты дремлешь, друг прелестный —
Пора, красавица, проснись:
Открой сомкнуты негой взоры
Навстречу северной Авроры,
Звездою севера явись!
Вечор, ты помнишь, вьюга злилась,
На мутном небе мгла носилась;
Луна, как бледное пятно,
Сквозь тучи мрачные желтела,
И ты печальная сидела —
А нынче... погляди в окно:
Под голубыми небесами
Великолепными коврами,
Блестя на солнце, снег лежит;
Прозрачный лес один чернеет,
И ель сквозь иней зеленеет,
И речка подо льдом блестит.
Вся комната янтарным блеском
Озарена. Веселым треском
Трещит затопленная печь.
Приятно думать у лежанки.
Но знаешь: не велеть ли в санки
Кобылку бурую запречь?
Скользя по утреннему снегу,
Друг милый, предадимся бегу
Нетерпеливого коня
И навестим поля пустые,
Леса, недавно столь густые,
И берег, милый для меня.'''

res = re.findall(r'\.{2,}', some_str)
print(f"Найдено {len(res)} совпадений")
