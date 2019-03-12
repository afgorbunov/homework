# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 05:48:05 2019
"""

person1 = {'card': 4276123465440000, 'pin': 9090, 'money': 100.90}
person2 = {'card': 4276123465440001, 'pin': 9091, 'money': 200.90}
person3 = {'card': 4276123465440002, 'pin': 9092, 'money': 300.90}

bank = [person1, person2, person3]


def get_person_by_card(card_number):
    for person in bank:
        if person['card'] == card_number:
            pass
            return person
    return None


def is_pin_valid(person, pin_code):
    if person['pin'] == pin_code:
        return True
    return False


def check_account(person):
    return round(person['money'], 2)


def withdraw_money(person, money):
    if person['money'] - money >= 0:
        person['money'] -= money
        return 'Вы сняли {} рублей. Остаток на счете составил {} рублей'.format(money, person['money'])
    else:
        return 'На вашем счету недостаточно средств!'


def process_user_choice(choice, person):
    if choice == 1:
        print(check_account(person))
    elif choice == 2:
        count = float(input('Сумма к снятию:'))
        print(withdraw_money(person, count))

def print_error(err_list):
    if len(err_list):
        print('\n'.join(['!!! '+e for e in err_list]))
        err_list = []

def start():
    card_number, pin_code = input('Введите номер карты и пин код через пробел:').split()

    error = []

    if card_number.isdigit():
        card_number = int(card_number)
        if pin_code.isdigit():
            pin_code = int(pin_code)
        else:
            error.append('Введен некорректный пароль.')
        person = get_person_by_card(card_number)
    else:
        error.append('Введен некорректный номер счета.')

    print_error(error)

    if person and is_pin_valid(person, pin_code):
        while True:
            choice = input('Выберите пункт:\n'
                               '1. Проверить баланс\n'
                               '2. Снять деньги\n'
                               '3. Выход\n'
                               '---------------------\n'
                               'Ваш выбор:')
            if choice.isdigit() and len(choice) == 1:
                choice = int(choice)
                if choice < 1 or choice > 3:
                    error.append('Введен некорректный пункт меню. Введите номер пункта от 1 до 3')
            else:
                error.append('Введен некорректный пункт меню. Введите номер пункта от 1 до 3')
            if choice == 3:
                break
            process_user_choice(choice, person)
            print_error(error)
    else:
        print('Номер карты или пин код введены не верно!')

start()
