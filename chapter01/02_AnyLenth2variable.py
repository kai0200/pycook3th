# -*- coding: utf-8 -*-
# vim: expandtab softtabstop=4 shiftwidth=4

"""
从任意长度的可迭代对象中分解元素
"""


def drop_first_last(grades):
    first, *middle, last = grades
    return (middle)


data = ['id', 'zhangsan', 'tall', '010-119110', 'token']
print(drop_first_last(data))

recode = ('John', 'dave@example.com', '010-62727433', '86-17911118888')
name, email, *phone_number = recode
print(*phone_number)
