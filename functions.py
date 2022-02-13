# -*- coding: utf-8 -*-

# Задание 1
"""
Создайте функцию get_summ(one, two, delimiter='&'),
которая принимает два параметра,
приводит их к строке и отдает объединенными через разделитель delimiter
"""


def get_summ(one, two, delimiter='&'):
    return one + delimiter + two


result = get_summ('Learn', 'Python')
print(result.title())
