#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дано число m (1 < m < 7). Вывести на экран название дня недели, который соответствует
# этому номеру

import sys

if __name__ == '__main__':

    m = 0

    if (m > 0 and m < 8):
        if (m == 1):
            print("Понедельник")
        if (m == 2):
            print("Вторник")
        if (m == 3):
            print("Среда")
        if (m == 4):
            print("Четверг")
        if (m == 5):
            print("Пятница")
        if (m == 6):
            print("Суббота")
        if (m == 7):
            print("Воскресенье")
    else:
        print("Ошибка!", file=sys.stderr)
        exit(1)
