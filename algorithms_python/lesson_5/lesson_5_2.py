# -*- coding: utf-8 -*-
"""Created on Sat Apr 13 07:19:12 2019."""

# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это
# цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как
# [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера:
# [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


def read_hex(num):
    strhex = input(f'\tчисло {str(num)}: ')
    err = []
    for s in strhex:
        if (not s.isdigit()) and (ord(s) < 65 or (ord(s) > 70 and ord(s) < 97) or ord(s) > 102):
            err.append(s)
    if len(err) > 0:
        print('Ошибка! Введены некорректные символы: "' + '", "'.join(err)+'"')
        return read_hex(num)
    else:
        return list(strhex)


def hex2dec(listhex):
    return int(''.join(listhex), 16)


def dec2hex(num):
    return list(hex(num)[2:])


if __name__ == '__main__':
    print('Введите два шестнадцатеричных числа:')
    a = read_hex(1)
    b = read_hex(2)
    res = []
    act = input('Введите обозначение математического действия (поддерживаются '
                'все основные действия - +, -, *, /): ')
    if act == '+':
        res = dec2hex(hex2dec(a)+hex2dec(b))
    elif act == '-':
        res = dec2hex(hex2dec(a)-hex2dec(b))
    elif act == '*':
        res = dec2hex(hex2dec(a)*hex2dec(b))
    elif act == '/':
        res = dec2hex(hex2dec(a)/hex2dec(b))
    else:
        print('Введен неверный символ математического действия')
    if len(res) > 0:
        print('Ответ: ', ''.join(res))
