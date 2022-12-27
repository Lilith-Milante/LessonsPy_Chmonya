from OOP_H7.hot_drink import HotDrink


class HotDrinkHeir(HotDrink):
    """наследник горячих напитков, субкласс"""

    def __init__(self, temperature, name, price, volume):
        super().__init__(name, price, volume)
        self.temperature = temperature

    def get_temperature(self):
        return self.temperature

    def get_name(self):
        return self.get_name()

    def get_price(self):
        return self.get_price()

    def get_volume(self):
        return self.get_volume()

    def build(self):
        print("Напиток " + self.name + " объёмом " + str(self.volume) + " с температурой " + str(self.temperature)\
              + " по цене " + str(self.price))

    def __str__(self):
        return f'Напиток {self.name} объёмом {self.volume} с температурой {self.temperature} по цене {self.price}'
