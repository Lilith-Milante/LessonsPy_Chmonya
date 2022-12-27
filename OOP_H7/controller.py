from OOP_H7.get_data import get_data
from OOP_H7.hot_drink_heir import HotDrinkHeir
from OOP_H7.input_data import input_data
from OOP_H7.request_drink import request


def start():
    #hot_drink_heir1 = HotDrinkHeir(80, "кофе", 120, 0.4)
    #hot_drink_heir2 = HotDrinkHeir(90, "какао", 110, 0.4)
    #hot_drink_heir3 = HotDrinkHeir(80, "шоколад", 130, 0.3)

    #hot_drink_heir1.build()  # печать через метод
    #print(hot_drink_heir1)  # печать через метод _str_
    #print(hot_drink_heir2)
    #print(hot_drink_heir3)

    message = int(input('Enter number:\n1 - to choice hotdrink - \n2 - to add hotdrink - \n'))
    if message == 1:
        found = get_data()
        fnd = request(found)

    if message == 2:
        new_data = input_data()
