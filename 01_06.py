__author__ = 'dimasik'
a = '412343342323'
L = list(a)
k = 0
for x in L:
    k = k + int(x)
print {'Sum': k,'Count': len(a)}