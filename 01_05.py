# -*- coding: utf-8 -*-
__author__ = 'Dimasik'
# На кириллицу ругался и пришлось использовать транслит?
# А всего-то надо было строчку добавить.

import math
w = int(raw_input('Vvedite shiriny: '))
h = int(raw_input('Vvedite dliny: '))
d = int(raw_input('Vvedite diametr: '))
sp= w*h
print 'Ploshad pryamoygolnika: ', sp
sk= math.pi*d**2/4
print 'Ploshad kruga: ', sk
if sk>sp:
    print 'plochady kruga bolshe,ne proneset kovrik '
elif sk<sp:
    print'ploshady kruga menche,proneset kovrik'
else: print 'oni ravhi'