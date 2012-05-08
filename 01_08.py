# -*- coding: utf-8 -*-
__author__ = 'slaer'
def enterSum(sum):
    money = str(sum)
    if len(money) <= 5:
        for number in money:
            if number == str(1): ten_thousand += 1
            if number >= str(5):
                for number in L['1','2','3','4','5']:
                    if number == L[0]: thousand += 1
                    elif number == L[1]: thousand += 2
                    elif number == L[2]: thousand += 3
                    elif number == L[3]: three_thousand += 1
                    else: five_thousand+= 1
            if number >= str(3):
                for number in L['1','2','3','4','5','6','7','8','9']:
                    if number == L[0]: hundred += 1
                    elif number == L[1]: hundred += 2
                    elif number == L[2]: hundred += 3
                    elif number == L[3]: hundred += 4
                    elif number == L[4]: five_hundred +=1
                    elif number == L[5]: five_hundred +=1; hundred += 1
                    elif number == L[6]: five_hundred +=1; hundred += 2
                    elif number == L[7]: five_hundred += 1; hundred += 3
                    else: five_hundred += 1; hundred += 4
            if number >= str(2):
                for number in L['1','2','3','4','5','6','7','8','9']:
                    if number == L[0]: ten += 1
                    elif number == L[1]: ten += 2
                    elif number == L[2]: ten += 3
                    elif number == L[3]: ten += 4
                    elif number == L[4]: fifty +=1
                    elif number == L[5]: fifty +=1; ten += 1
                    elif number == L[6]: fifty +=1; ten += 2
                    elif number == L[7]: fifty += 1; ten += 3
                    else: fifty += 1; ten += 4
    if len(money) == 4: ten_thousand, five_thousand, thousand, five_hundred, hundred, fifty, ten = \
                        thousand, five_hundred, hundred, fifty, ten, fifty, ten
    if len(money) == 3: ten_thousand, five_thousand, thousand, five_hundred, hundred, fifty, ten = \
                        hundred, fifty, ten, fifty, ten, fifty, ten
    print {'ten_thousand': ten_thousand, 'five_thousand': five_thousand, 'thousand': thousand,
           'five_hundred': five_hundred, 'hundred': hundred, 'fifty': fifty, 'ten': ten}
    return ten_thousand,five_thousand,thousand,five_hundred,hundred,fifty,ten

enterMoney = raw_input('Enter your money: ')
enterSum(enterMoney)

