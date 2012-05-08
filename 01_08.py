# -*- coding: utf-8 -*-
__author__ = 'slaer'
def enterSum(sum):
    money = str(sum)
    moneyList = []
    [moneyList.append(number) for number in money]
    moneyList.reverse()
    global ten_thousand, five_thousand, thousand, five_hundred, hundred, fifty, ten, i, tail
    ten_thousand, five_thousand, thousand, five_hundred, hundred, fifty, ten, i, tail = 0, 0, 0, 0, 0, 0, 0, 0, 0
    for number in moneyList:
        i += 1
        if i == 1:                              # Подсчет остатка, например 5 рублей ( он не выдается:) )
            tail = number
            continue

        if i == 2 and number == '0': continue   # Подсчет количества 10 рублевых купюр и 50 рублевых
        if i == 2 and number < '5':
            ten += int(number)
        elif i == 2 and number == '5' :
            fifty += 1
        elif i == 2 and number > '5':
            fifty += 1
            ten = 5 - (10 - int(number))

        if i == 3 and number == '0': continue   # Подсчет количества 100 рублевых купюр и 500 рублевых
        if i == 3 and number < '5':
            hundred += int(number)
        elif i == 3 and number == '5':
            five_hundred += 1
        elif i == 3 and number > '5':
            five_hundred += 1
            hundred = 5 - (10 - int(number))

        if i == 4 and number == '0': continue   # Подсчет количества 1000 купюр и 5000
        if i == 4 and number < '5':
            thousand += int(number)
        elif i == 4 and number == '5':
            five_thousand += 1
        elif i == 4 and number > '5':
            five_thousand += 1
            thousand = 5 - (10 - int(number))

        if i == 5: ten_thousand += 1
        if len(moneyList) == i: break

print 'Max money is 15000 in day'               # Макимум в 1 день можно выдать только меньше 15 тысяч
x = 0
while x == 0:
    enterMoney = int(raw_input('Enter your money: '))
    if enterMoney > 15000:
        print 'MAX MONEY IS 15000! Please try again!'
        continue
    else: x = 1

enterSum(enterMoney)                            # Подсчет всех количества купюр и вывод на экран
print {'Ten thousand': ten_thousand, 'Five Thousand': five_thousand, 'Thousand': thousand,
       'Five hundred': five_hundred, 'Hundred': hundred, 'Fifty': fifty, 'Ten': ten}
print 'Tail is: ', tail

