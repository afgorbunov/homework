# -*- coding: utf-8 -*-
"""Created on Mon Apr  1 04:33:15 2019."""


def input_int(message):
    inp = input(message)
    if inp.isdigit():
        return int(inp)
    else:
        print('Введенное значение не является числом')


def task_2():
    inp = input('Введите целое многозначное число: ')
    odd = 0
    even = 0
    for n in inp:
        if int(n) % 2 == 0:
            even += 1
        else:
            odd += 1
    print(f'Число содержит {even} четных цифр и {odd} нечетных')


def task_3():
    inp = input('Введите целое многозначное число: ')
    print(
        'Реверсивное число будет следующим: '
        f"{''.join([inp[n] for n in range(-1,-len(inp)-1,-1)])}")


def task_4():
    inp = input_int('Введите число расчитываемых элементов: ')
    for i in range(inp):
        if i == 0:
            prev = 1
        else:
            prev /= -2
        print(f'\t{i+1:2d} {prev}')


def task_5():
    print('Таблица ASCII'.center(79, ' '))
    c = 32
    while c <= 127:
        string = ''
        for i in range(10):
            string += f'{c:3d} {chr(c)}  '
            c += 1
            if c > 127:
                break
        print(string)


def task_9():
    inp = input('Введите последовательность чисел через пробел: ')
    inp_list = inp.split(' ')
    data = {}
    for n in inp_list:
        summ = 0
        if n.isdigit():
            for s in n:
                summ += int(s)
        data[n] = summ
    maxsum = sorted(data.values())[-1]
    maxnum = [k for k, v in data.items() if v == maxsum]
    print('Наибольшая сумма для следующих чисел:')
    for n in maxnum:
        print(f'Число {n}, сумма {data[n]}')


if __name__ == '__main__':
    print(' Задания к уроку №2 '.center(79, '='))
    print(' Задача №2 '.center(79, '-'))
    task_2()
    print(' Задача №3 '.center(79, '-'))
    task_3()
    print(' Задача №4 '.center(79, '-'))
    task_4()
    print(' Задача №5 '.center(79, '-'))
    task_5()
    print(' Задача №9 '.center(79, '-'))
    task_9()
    print('='*79)
