# -*- coding: utf-8 -*-
__author__ = 'slaer'
# Сразу о кириллице: с одной сторону кириллица врода нам особо не нужна, но даже
# если будут комментарии с иной кодировкой - будет ошибка. Что бы этого избежать
# как раз и нужна первая строка строка. TODO: запомнить первую строку

# Программы мы не пишем просто так - важно этим пользоваться.
# Вот представим, что этим кодом надо будет пользоваться несколько раз
# Для различного количества списков L.
# Надо переписать, используя функцию. Например так:

def getMaxSeqInTuple(tupleIn):
    # Название функции - это описание того, что она делает.
    # Чем точнее название - тем проще с этой функцией работать. Переименовать
    # функцию в PyCharm можно всегда (это не сложно - изпользуя опцию Refactor → Rename).
    # Тоже самое относится и к переменным - не надо бояться длинных названий.

    # Кстати об IDE: если вдруг мы ввели функцию или, наоборот, решили, что какой-нибудь
    # Цикл не нужен — а, соответственно, надо убирать или добавлять кучу отступов вручную, то
    # pyCharm тут поможет:
    # 1. выделяя блок текста, нажимаем «Tab» — появляется отступ
    # 2. выделяя блок текста, нажимаем «Shift + Tab» — один отступ исчезает

    # По такой строке: эт не паскаль — тут не надо объявлять переменные. Просто
    # в некоторых случаях (переменная count, например) нам надо прибавлять к еще
    # «не готовой» переменной — соответственно мы заранее присваем этой переменной начальное
    # значение. ТУДУ: убрать лишние переменные :
    #count, maxCount, i, x, number = 0, 0, 0, 0, []    # !!!Убрал k, maxNumber
    count, maxCount, x, number, maxNumber = 0, 0, 0, [], 0
                # TODO: [разобраться и заменить TODO → ТУДУ] можно i убирать:
                # ибо i — инициализируется в цикле
                # x — из-за сравнения
                # count — надо оставить — ибо применяется оператор +=
                # maxCount —  сравнение с нулем должно быть — можно избежать,
                # но пусть в разборе останется — функция более оптимально написанная есть
                # остается number — ибо к нему применяется append,
                # а к несуществующему append применяться не может
                #
                # а вот maxNumber стоит оставить — для случая с пустым списком —
                # если на вход послать [], то выдаст ошибку.
                #
                # Переменных слишком много — и это плохо, хотя и не ошибка.

    sortedList = list(tupleIn)
    sortedList.sort()

    #print sortedList               # В готовой функции print лишний — его допустимо
                                    # использовать только для отладки

    # Тут посмотрите как было: два цикла с одинаковыми условиями.
    # Один цикл я бы просто убрал — плох он там (да и как-то станен)
    for i in sortedList:
        if i == x:
            number.append(i)
        x = i

    for i in sortedList:            # ТУДУ: Разобраться почему строка лишняя и удалить ее
                                    # На самом деле лишняя строчка с циклом, а не pass, хотя
                                    # pass тоже лишний. Просто цикл получается дважды идет по
                                    # одним и тем же значениям.
        if i in number:
            count += 1
            if count > maxCount:    #!!! Поменял знак условия if на ">", следовательно "pass" убрался
                #pass               # Лишний pass — можно обойтись и без него
                maxCount = count
                maxNumber = i
        else:
            count = 0               # в целом работает, хотя и не красиво

    return {'Number': maxNumber, 'Counts': maxCount}
    # за интерфесом лучше следить — в задании было «number» и «count»
    # Вполне может оказаться, что какая-либо другая процедура требует ключи
    # именнно в таком виде

# Напишу функцию со своим видением алгоритма
def getMaxSeqInTupleOther(tupleIn):
    incSortedList = list(tupleIn)       # Типа — возрастающе отсортированный список
    incSortedList.sort()

    currentNumber = 0
    currentCount = 0
    resultDict = {'number': 0, 'count': 0}      # Очевидно, что в начале словарь пустой

    for item in incSortedList:
        if item == currentNumber:
            currentCount += 1
        else:
            if currentCount > resultDict['number']:
                resultDict['number'] = currentNumber
                resultDict['count'] = currentCount
                currentCount = 0
            currentNumber = item

    return resultDict


# для отладки добавил в список 0 и 4
L = (0, 4, 4, 23, 23, 12, 16, 56, 18, 13, 23, 24, 17, 34, 12, 34, 5, 6, 23, 23, 81, 14)
print getMaxSeqInTuple(L)
print getMaxSeqInTupleOther(L)
