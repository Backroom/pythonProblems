__author__ = 'Dimasik'
L1 = [4, -1, -3, 12, 8, 8, -1, 11, 8, -6, 9, 10, -2, 15, 6, 7, 12, -7, 9, -7]
LM, LP = [], []
for i in L1:
    if i < 0:
        LM.append(i)
    else: LP.append(i)
res = tuple([LM] + [LP])
print res