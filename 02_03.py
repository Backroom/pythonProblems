# -*- coding: utf-8 -*-
__author__ = 'slaer'
import random
marksStudents = []
mark = 0
taskDict = {str(key): random.choice('abcdef') for key in range(1,21)}
answerDict = {str(key): random.choice('abcdef') for key in range(1,21)}
for k, v in taskDict.iteritems():
    if (k in answerDict.keys()) and (v in answerDict.values()):
        marksStudents.append((k,v))
        mark += 1
print taskDict
print answerDict
print marksStudents
print mark
