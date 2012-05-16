# -*- coding: utf-8 -*-
__author__ = 'slaer'
import random
IdeaDictTrigger = {man: int(random.choice('123')) for man in ['Jerry','Mark','Tom']}
print IdeaDictTrigger
NumberingDict, number = {}, 0
def giveTaskNumber(man):                                                #2. Функция берет чела которого осенило,
    global NumberingDict, name, number                                  #   добавляет его в словарь и дает номер задачи
    number += 1
    name = list(man)[0]
    NumberingDict[name] = number
    return NumberingDict,number
for man in IdeaDictTrigger.items():                                     #1. Если у чела значение равно "Двум",
        if 2 in man:                                                    #   значит его осенило и он придумал задачу:)
            giveTaskNumber(man)
if len(NumberingDict.items()) == 1:
    print NumberingDict, 'Придумал задачку'
elif len(NumberingDict.items()) > 1: print NumberingDict, 'Придумали задачи'
else: print 'Никто ниче не придумал :('