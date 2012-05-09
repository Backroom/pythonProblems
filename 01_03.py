# -*- coding: utf-8 -*-
__author__ = 'slaer'
M = (0,0,1,0,1,0,0)
L = (17, 40, 65, 24, 12, 13, 42)
#Result L1 = (0, 0, 65, 0, 12, 0, 0)#
MM,LL = list(M),list(L)
L1,c,k = [],L[0],0
for i in MM:
    k += 1
    if k == 3:
        c = LL[2]
    elif k == 5:
        c = LL[4]
    else: c = L[0]
    L1.append(i*c)
print 'First list: ', MM
print 'Second list: ', LL
print 'Result: ', L1

# Надо все проще:

def setMaskToTuple(tupleIn, mask):
    resultList = []
    for i in xrange(len(tupleIn)):
        if mask[i] == 0:
            resultList.append(0)
        else:
            resultList.append(tupleIn[i])

    resultTuple = tuple(resultList)
    return resultTuple

# Опять-таки смотрите формулировку задачи — на вход два кортежа и один на выходе
# TODO: добавить обработку такой ситуации, когда длины кортежей не равны меду собой
# TODO: напомнить мне[Karpov], что бы я показал немного черной магии с этим примером


print setMaskToTuple(L, M)
