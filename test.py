from random import *

buy = {"Вино":randint(1, 7)*5, 
        "Сахар":randint(5, 9)*5, 
        "Оружие":randint(3, 12)*5,
        "Украшения":randint(5, 18)*5,
        "Рабы":randint(4, 15)*5,
        }
for item in buy:
    print(item)