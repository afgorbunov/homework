# -*- coding: utf-8 -*-
"""Created on Sun Mar 31 05:01:44 2019."""

from random import randint, choice


def gen_upper_case():
    return chr(randint(65, 90))                                                # создается временная переменная типа str размером 8 бит


def gen_lower_case():
    return chr(randint(97, 122))                                               # создается временная переменная типа str размером 8 бит


def gen_digit():
    return chr(randint(48, 57))                                                # создается временная переменная типа str размером 8 бит


def gen_symbol():
    gen_funcs = [                                                              # список со ссылками на функции
        gen_upper_case,
        gen_upper_case,
        gen_digit,
    ]
    return choice(gen_funcs)()                                                 # возврат результата вызова случайно выбранной функции (один случайный символ)


def gen_login():
    return ''.join([gen_symbol() for i in range(randint(4, 8))])               # возврат строки из случайных символов длинной от 4 до 8 символов по 8 бит


def gen_pincode():
    return ''.join([gen_digit() for i in range(4)])                            # возврат строки из случайных чисел длинной 4 символа по 8 бит


def gen_string():
    return f'{gen_login()}\t{gen_pincode()}'                                   # возврат строки с парой логин/пароль - строка от 9 до 13 символов по 8 бит


def gen_pinfile(count_strings):
    from os import path as osp
    p = osp.join(osp.abspath(osp.join(__file__, '..')), 'login_pin.txt')       # создание строки с путем сохранения файлов
    outfile = open(p, 'w', encoding='utf-8')                                   # создание ссылки на файл
    outfile.write("\n".join([gen_string() for i in range(count_strings)]))     # создание строки со всем текстом; запись в файл
    outfile.flush()
    outfile.close()


gen_pinfile(10_000)
