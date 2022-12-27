class HotDrink:
    """Описание напитка"""

    def __init__(self, name, price, volume):
        self.name = name
        self.price = price
        self.volume = volume

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_volume(self):
        return self.volume

    def build(self):
        print("Напиток " + self.name + " объёмом " + str(self.volume) + " по цене " + str(self.price))

    def __str__(self):
        return f'Напиток {self.name} объёмом {self.volume} по цене {self.price}'


HotDrink1 = HotDrink("шоколад", 120, 0.4)
HotDrink2 = HotDrink("какао", 110, 0.3)