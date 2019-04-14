# -*- coding: utf-8 -*-
"""Created on Fri Apr 12 05:31:10 2019."""

from statistics import mean
import collections


def inp_compamies(dict_len):
    res = dict()
    Company = collections.namedtuple(
        'Company', ['k1', 'k2', 'k3', 'k4', 'avg'])
    for i in range(dict_len):
        print(f'Введите данные для организации №{i+1}')
        caption = input('\tназвание: ')
        print('\tприбыль за...')
        data = [float(input(f'\t\t{k} квартал: ')) for k in range(1, 5)]
        res[caption] = Company(*data, mean(data))
    return res


def main():
    dict_len = int(input('Введите количество вводимых компаний: '))
    companies = inp_compamies(dict_len)
    avgall = mean([c.avg for c in companies.values()])
    print('предприятия, чья среднегодовая прибыль выше средней:\n',
          '\t'+'\n\t'.join([c for c, v in companies.items()
                            if v.avg >= avgall]),
          '\nпредприятия, чья среднегодовая прибыль ниже средней:\n',
          '\t'+'\n\t'.join([c for c, v in companies.items()
                            if v.avg < avgall]),
          )


if __name__ == '__main__':
    main()
