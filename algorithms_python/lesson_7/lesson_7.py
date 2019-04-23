# -*- coding: utf-8 -*-
"""Created on Sat Apr 20 04:44:34 2019."""

from random import randint
from random import uniform


def get_random_array(minel, maxel, lenarr, type=int):
    if type == int:
        return [randint(minel, maxel-1) for _ in range(lenarr)]
    elif type == float:
        return [uniform(minel, maxel-1) for _ in range(lenarr)]


def print_array(array):
    print(' '.join(map(lambda x: f'{x:.2f}' if type(
        x) == float else str(x), array)))


def input_int(ref):
    raw = input(ref)
    while not raw.isdigit():
        print(f'!!! Введенное значение "{raw}" не является числом. '
              'Повторите ввод!')
        raw = input(ref)
    return int(raw)


def bubble_sort(arr):
    is_sorted = True
    for j in range(len(arr)):
        for i in range(len(arr)-1-j):
            if arr[i] < arr[i+1]:
                is_sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]
        if is_sorted:
            break
    return arr


def merge(arr1, arr2):
    i1 = 0
    i2 = 0
    res = []
    is_sorted = False
    while not is_sorted:
        if i1 == len(arr1):
            res += arr2[i2:]
            is_sorted = True
        elif i2 == len(arr2):
            res += arr1[i1:]
            is_sorted = True
        elif arr1[i1] > arr2[i2]:
            res.append(arr2[i2])
            i2 += 1
        elif arr1[i1] <= arr2[i2]:
            res.append(arr1[i1])
            i1 += 1
    return res


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        point = len(arr)//2
        left = arr[:point]
        right = arr[point:]
        return merge(merge_sort(left), merge_sort(right))


def task_1():
    print(' Задача 1 '.center(79, '='))
    array = get_random_array(-100, 100, input_int('Введите длину массива: '))
    print('Исходный массив:')
    print_array(array)
    array = bubble_sort(array)
    print('Отсортированный массив:')
    print_array(array)


def task_2():
    print(' Задача 2 '.center(79, '='))
    array = get_random_array(0, 50, input_int(
        'Введите длину массива: '), type=float)
    print('Исходный массив:')
    print_array(array)
    array = merge_sort(array)
    print('Отсортированный массив:')
    print_array(array)


def task_3():
    # задача решена через сортировку слиянием, так как данный метод не
    # рассматривался на уроках
    print(' Задача 3 '.center(79, '='))
    array = get_random_array(0, 50, 2*input_int('Введите опорное число: ')+1)
    print('Исходный массив:')
    print_array(array)
    array = merge_sort(array)
    print('Отсортированный массив:')
    print_array(array)
    print(f'Медианой является число {array[len(array)//2]}')


if __name__ == '__main__':
    task_1()
    task_2()
    task_3()
