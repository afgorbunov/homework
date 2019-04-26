# -*- coding:utf-8 -*-


def task_1():
    num = input('Введите трехзначное число: ')
    numlist = list(num)
    summ = 0
    mult = 1
    for i in numlist:
        summ += int(i)
        mult *= int(i)
    print(
        f'Результаты:\n\tсумма цифр числа = {summ}'
        '\n\tпроизведение цифр числа = {mult}')


def task_3():
    p1 = input('Введите координаты точки 1 через пробел в формате "x y": ')
    p2 = input('Введите координаты точки 2 через пробел в формате "x y": ')
    p1 = [int(i) for i in p1.split(' ')]
    p2 = [int(i) for i in p2.split(' ')]
    k = (p1[1] - p2[1])/(-(p2[0] - p1[0]))
    b = (p1[0]*p2[1] - p2[0]*p1[1])/(-(p2[0] - p1[0]))
    print(f"Уравнение прямой: y = {k:.2f}x{'+' if b>=0 else ''}{b:.2f}")


def task_4():
    from random import randint
    rng = input('Введите диапазон генерации случайного целого числа через '
                "пробел в формате \"min max\": ")
    rng = [int(i) for i in rng.split(' ')]
    print(f'Случайное целое число: {randint(*rng)}')
    from random import uniform
    rng = input('Введите диапазон генерации случайного вещественного числа '
                "через пробел в формате \"min max\": ")
    rng = [float(i) for i in rng.split(' ')]
    print(f'Случайное вещественное число: {randint(*rng):.2f}')
    rng = input('Введите диапазон генерации случайного символа через '
                "пробел в формате \"min max\": ")
    rng = [ord(i) for i in rng.split(' ')]
    print(f'Случайный символ: {chr(randint(*rng))}')


def diff_task_1():
    from collections import Counter
    datafile = open(r'.\login_pin.txt', 'r', encoding='utf-8')
    passwd_list = [l.replace('\n', '').split('\t')[1]
                   for l in datafile.readlines()]
    c = Counter(passwd_list)
    popul = sorted(c, key=c.__getitem__, reverse=True)
    ten_popul = [f'"{p}" - повторяется {c[p]} раз' for p in popul[:10]]
    crlf = '\n\t'
    print('Наиболее популярные пароли в файле:\n' +
          f'\t{crlf.join(ten_popul)}')


if __name__ == '__main__':
    print(' Задание №1 '.center(79, '='))
    task_1()
    print(' Задание №3 '.center(79, '='))
    task_3()
    print(' Задание №4 '.center(79, '='))
    task_4()
    print(' Дополнительное задание №1 '.center(79, '='))
    diff_task_1()
    print('='*79)
