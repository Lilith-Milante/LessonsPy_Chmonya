import time

# 1. Создать класс TrafficLight (светофор):
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
# зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго
# (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке
# (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.

class TrafficLight():
    __color = 0

    def __init__(self):
        self.mode = 0

    def running (self, red, yellow, green):

        while self.mode < 3:
            if self.mode == 0:
                TrafficLight.__color = red
                print('red')
                time.sleep(7)
                self.mode += 1
            elif self.mode == 1:
                TrafficLight.__color = yellow
                print('yellow')
                time.sleep(2)
                self.mode += 1
            if self.mode == 2:
                TrafficLight.__color = green
                print('green')
                time.sleep(3)
                self.mode += 1


exs = TrafficLight()
exs.running()


# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра
# дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# проверить работу метода.