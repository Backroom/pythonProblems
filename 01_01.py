# -*- coding: utf-8 -*-
__author__ = 'Dimasik'

# Программы мы не пишем просто так - важно этим пользоваться.
# Вот представим, что этим кодом надо будет пользоваться несколько раз
# Для различного количества списков L.
# Надо переписать, используя функцию. Например так:

def setDictMinMaxAvgFromTuple(tupleIn):
    # Комментарий: название функции - это описание того, что она делает.
    # Чем точнее название - тем проще с ней вообще работать. Переименовать
    # функцию можно всегда (это не сложно).
    # Тоже самое относится и к переменным.

    # tupleSum = 0.0    # Вот фактически первая ошибка
                        # Ну и лишнее напоминание про название для переменных
    tupleSum = 0        # !!!Исправил значение переменной turpleSum на тип Int
    for i in L:
        tupleSum += i   # Лучше использовать оператор "+=" - это повышает читабельность кода
    print tupleSum      # Такой принт полезен при отладке (это так и называется - отладка принтами),
                        # но в итоговом коде это необходимо убирать

    # x = 0               #
    # for i in L:         # Это вторая ошибка
    #    x = x+1          #
    x = len(L)            # !!!Думаю так лучше подсчитать количество элементов

    return {'min': min(tupleIn), 'max': max(tupleIn), 'average': tupleSum/x}


L = (4, 12, 16, 56, 23, 24, 17, 34, 12, 34, 5, 6, 23,18)
D = setDictMinMaxAvgFromTuple(L)
print D

# TODO: 1. Разобраться с коментариями, добавленными в коде
# TODO: 2. Исправить ошибку, в 15 строке (фактически первая ошибка)
#       Среднее на самом деле получается 20.286 - подобные неточности могут приводит
#       к серьезным ошибкам
# TODO: 3. На строках 23-24 лишний цикл. Не ошибка, но исправить надо.
#
# ps TODO: как напоминание: каждое исправление отдельным коммитом
# pps TODO: сразу забыл: посмотреть на самую верхнюю строчку
#       Такая строка применяется, если мы используем кириллицу (даже точнее utf-8)
#       в программе - это помогает избежать ошибки при выполнении