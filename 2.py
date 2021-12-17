#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Из трех действительных чисел a, b и c выбрать те, модули которых не меньше 4.

if __name__ == '__main__':

    a = input("enter number - a")
    b = input("enter number - b")
    c = input("enter number - c")

    if(abs(a) > 4):
        print(a)
    if(abs(b) > 4):
        print(b)
    if(abs(c) > 4):
        print(c)
