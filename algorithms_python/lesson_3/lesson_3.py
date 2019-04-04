# -*- coding: utf-8 -*-
"""Created on Tue Apr  2 22:16:17 2019."""


from collections import Counter


def input_list(desp, isint=True):
    inp = input(desp)
    if isint:
        res = []
        for i in inp.split(' '):
            if i.isdigit():
                res.append(int(i))
            else:
                print(f'Введенное значение "{i}" не является числом')
        return res
    return inp.split(' ')


def task_2():
    inplist = input_list('Введите массив целых чисел через пробел: ')
    res = [i for i in range(len(inplist)) if inplist[i] % 2 == 0]
    for i in range(len(res)):
        print(f'Индекс {res[i]}\tЗначение {inplist[res[i]]}')


def task_4():
    inplist = input_list('Введите массив целых чисел через пробел: ')
    c = Counter(inplist)
    res = sorted(c.items(), key=(lambda x: x[1]), reverse=True)[0]
    print(f'Самый часто встречающийся элемент "{res[0]}", который '
          f'встречается {res[1]} раз.')


def task_6():
    inplist = input_list('Введите массив целых чисел через пробел: ')
    indx = inplist.index(max(inplist)), inplist.index(min(inplist))
    indx = sorted(indx)
    summ = 0
    for i in range(indx[0]+1, indx[1]):
        summ += inplist[i]
    print('Сумма между минимальным и максимальным элементами введенного '
          f'массива равна {summ}')


def task_8():
    rawlists = [input_list(
        f'Введите массив из 4х целых чисел через пробел [{i}]: '
    ) for i in range(4)]
    matrix = [[None]*5 for i in range(4)]
    for l in range(len(rawlists)):
        if len(rawlists[l]) > 4:
            matrix[l][:4] = rawlists[l][:4]
        else:
            [rawlists[l].append(0)
                for i in range(4-len(rawlists[l]))
             ]
            matrix[l][:4] = rawlists[l]
    for l in matrix:
        summ = 0
        for i in range(4):
            summ += l[i]
        l[4] = summ
        print(' '.join([str(i).rjust(4) for i in l]))


if __name__ == '__main__':
    print(' Задачи урока №3 '.center(79, '='))
    task_2()
    print('='*79)
    task_4()
    print('='*79)
    task_6()
    print('='*79)
    task_8()
    print('='*79)
