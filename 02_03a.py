# -*- coding: utf-8 -*-
__author__ = 'JLan'

# Это строка верных ответов:
vAns = 'abeabccbdfcaabdadfce'

# Потом я в консоли запускал N раз следующую команду (первую так-то, но из
# тех, что есть — можно уже любую), где каждый раз с листочка переписывал
# строку с ответами.
# Тут по сути 4 равнозначных варианта. Если запустить — выведет 4 раза 9,
# что логично: верных ответов 9 в каждом случае

print len([x for x in map(lambda A, B: A==B, vAns, 'dfcaafbeabccbbdadfce') if x == True])

print sum(map(lambda A, B: A==B, vAns, 'dfcaafbeabccbbdadfce'))

print reduce(lambda x, y: x + y, map(lambda A, B: A==B, vAns, 'dfcaafbeabccbbdadfce'))

print len(filter(lambda x: x == True, map(lambda A, B: A==B, vAns, 'dfcaafbeabccbbdadfce')))


# Это вызов timeit и его оформление — таймит вызывает каждую функцию
# 1 миллион раз и выводит время, которое это занимает:
import timeit
functionList = [
    "len([x for x in map(lambda A, B: A==B, 'abeabccbdfcaabdadfce', 'dfcaafbeabccbbdadfce') if x == True])",
    "sum(map(lambda A, B: A==B, 'abeabccbdfcaabdadfce', 'dfcaafbeabccbbdadfce'))",
    "reduce(lambda x, y: x + y, map(lambda A, B: A==B, 'abeabccbdfcaabdadfce', 'dfcaafbeabccbbdadfce'))",
    "len(filter(lambda x: x == True, map(lambda A, B: A==B, 'abeabccbdfcaabdadfce', 'dfcaafbeabccbbdadfce')))"
]
for funcItem in functionList:
    print funcItem, ":"
    print timeit.timeit(funcItem)
