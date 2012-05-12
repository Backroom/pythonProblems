# -*- coding: utf-8 -*-
__author__ = 'Dimasik'
# На кириллицу ругался и пришлось использовать транслит?
# А всего-то надо было строчку добавить.

import math
P = ((5, 10), (7, 10), (3, 4), (8, 12), (6, 9))
K = (4, 12, 5, 9)
R = {5: ((5, 10), (7, 10), (8, 12), (6, 9))}
SP = []
SK = []
SS = {}
for x in P:
    print 'Площадь прямоугольника: ',x,'-',x[0]*x[1]
    SP.append(x[0]*x[1])
for x in K:
    print 'Площадь круга:', x, '-', math.pi*x**2/4
    SK.append(int(math.pi*x**2/4))
print SP
print SK
for k in SK:
   for p in SP:
       if k < p:
           SS[k] = p
print SS


