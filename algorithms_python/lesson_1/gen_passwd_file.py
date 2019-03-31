# -*- coding: utf-8 -*-
"""Created on Sun Mar 31 05:01:44 2019."""

from random import randint, choice


def gen_upper_case():
    return chr(randint(65, 90))


def gen_upper_case():
    return chr(randint(97, 122))


def gen_digit():
    return chr(randint(48, 57))


def gen_symbol():
    gen_funcs = [
        gen_upper_case,
        gen_upper_case,
        gen_digit,
    ]
    return choice(gen_funcs)()


def gen_login():
    return ''.join([gen_symbol() for i in range(randint(4, 8))])


def gen_pincode():
    return ''.join([gen_digit() for i in range(4)])


def gen_string():
    return f'{gen_login()}\t{gen_pincode()}'


def gen_pinfile(count_strings):
    from os import path as osp
    p = osp.join(osp.abspath(osp.join(__file__, '..')), 'login_pin.txt')
    outfile = open(p, 'w', encoding='utf-8')
    outfile.write("\n".join([gen_string() for i in range(count_strings)]))
    outfile.flush()
    outfile.close()


gen_pinfile(10_000)
