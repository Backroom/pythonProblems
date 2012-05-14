# -*- coding: utf-8 -*-
__author__ = 'slaer'
import random
marksStudents, mark = [], 0
taskDict = {key: random.choice('abcdef') for key in range(1,21)}
answerDict = {key: random.choice('abcdef') for key in range(1,21)}
listTaskDict, listAnswerDict = taskDict.items(), answerDict.items()
for i in listTaskDict:
    if i in listAnswerDict:
        marksStudents.append(i)
        mark += 1
print marksStudents
print 'Правильных ответов:', mark