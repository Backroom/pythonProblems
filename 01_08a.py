# -*- coding: utf-8 -*-
__author__ = 'jlan'

BANKNOTES_NOMINAL_LIST = (5000, 1000, 500, 100, 50, 10)

def getBanknotesCountFromSum(moneySum):
    nominalsDict = {}
    for nominal in BANKNOTES_NOMINAL_LIST:
        nominalsDict[nominal] = 0
        while moneySum > nominal:
            moneySum -= nominal
            nominalsDict[nominal] += 1
    nominalsDict['ost'] = moneySum
    return nominalsDict

print getBanknotesCountFromSum(5455)
print getBanknotesCountFromSum(4455)
print getBanknotesCountFromSum(17000)
print getBanknotesCountFromSum(400)
print getBanknotesCountFromSum(9999)



