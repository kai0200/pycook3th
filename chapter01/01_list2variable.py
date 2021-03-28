# -*- coding: utf-8 -*-
# vim: expandtab softtabstop=4 shiftwidth=4

"""
将序列分解为变量
"""


data = ['BeiJing', 11, 22, 55, (2021, 3, 28)]
city, _, _, _, (Y, M, D) = data
print(city, Y, M, D)

s = 'Hello!'
a, b, c, d, e, _ = s
print(a, b, c, d, e)
