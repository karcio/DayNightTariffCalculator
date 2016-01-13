'''
Created on Jan 13, 2016
simple day/night tariff calculator
@author: karol
'''

def calculate():
    day = counterState * 0.625 * D_TARIFF_COST
    night = counterState * 0.375 * N_TARIFF_COST
    calculation = day + night 
    return calculation
    
D_TARIFF_COST = 0.1436
N_TARIFF_COST = 0.0711 

counterState = input('Insert you counter measurement here: ')
print("Total cost per month: {0:.2f}".format(round(calculate() * 30, 2)))
print("Total cost per year : {0:.2f}".format(round(calculate() * 365, 2)))