# -*- coding: utf-8 -*-
"""Created on Sun Apr  7 07:11:59 2019."""

from datetime import datetime
from random import randint
from collections import Counter


def calc_time(func):
    def f(*args, **kwargs):
        begin = datetime.now()
        func(*args, **kwargs)
        end = datetime.now()
        delta = end - begin
        print(
            f'Время исполнения функции "{func.__name__}": '
            f'{delta.seconds}:{delta.microseconds}')
    return f


@calc_time
def compare_lists_1(a, b):
    """
    Сложность данного алгоритма - O(len(a)*len(b)) в худшем случае,
    так как циклы пробегают каждый элемент второго списка столько раз, сколько
    элементов содержит первый список.
    """
    res = 0
    for i in a:
        for j in b:
            if i == j:
                res += 1
                break
    print(f'Обнаружено совпадений: {res}')


@calc_time
def compare_lists_2(a, b):
    """
    Сложность данного алгоритма - O(len(a)), так как время выполнения зависит
    фактически только от длинны первого массива, если принебречь временем
    проверки элемента на вхождение во второй список.
    """
    res = 0
    for i in a:
        if i in b:
            res += 1
    print(f'Обнаружено совпадений: {res}')


@calc_time
def prime_numbers(m):
    res = []
    a = True
    for i in range(2, m+1):
        for j in range(2, i):
            if i % j == 0:
                a = False
                break
        if a:
            res.append(i)
        a = True
    print(f'Список простых чисел: {res}')
    print(f'Найдено простых чисел: {len(res)}')


@calc_time
def prime_sieve(m):
    res = list(range(2, m+1))
    i = 0
    while i < len(res):
        for j in range(res[i], res[-1]+1//res[i]):
            if res[i]*j in res:
                res.remove(res[i]*j)
        i += 1
    print(f'Список простых чисел: {res}')
    print(f'Найдено простых чисел: {len(res)}')


if __name__ == '__main__':
    size = 5000
    print(' Оценка сложности алгоритма проверки вхождения элементов одного '
          'списка в другой ')
    a = [randint(0, size*10) for i in range(size)]
    b = [randint(0, size*10) for i in range(size)]
    compare_lists_1(a, b)
    compare_lists_2(a, b)
    print('='*79)
    print(' Оценка сложности алгоритма поиска простых чисел ')
    m = 1000
    prime_numbers(m)
    prime_sieve(m)
