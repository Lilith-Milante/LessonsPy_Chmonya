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

    def __init__(self, red, yellow, green):
        self.mode = 0
        self.colors = [red, yellow, green]
        
    def running (self):
        
        while self.mode < 3:
            if self.mode == 0:
                TrafficLight.__color = self.colors[0]
                print('red')
                time.sleep(7)
                self.mode += 1
                
            elif self.mode == 1:
                TrafficLight.__color = self.colors[1]
                print('yellow')
                time.sleep(2)
                self.mode += 1
                
            elif self.mode == 2:
                TrafficLight.__color = self.colors[2]
                print('green')
                time.sleep(3)
            self.mode +=1

# 2 var           
exs = TrafficLight('red', 'yellow', 'green')

class TrafficLight():
    __color = 0

    def __init__(self, red, yellow, green):
        self.colors = [red, yellow, green]
        
    def running (self):

        TrafficLight.__color = self.colors[0]
        print(TrafficLight.__color)
        time.sleep(7)
        
        TrafficLight.__color = self.colors[1]
        print(TrafficLight.__color)
        time.sleep(2)

        TrafficLight.__color = self.colors[2]
        print(TrafficLight.__color)
        time.sleep(3)

exs = TrafficLight('red', 'yellow', 'green')

# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра
# дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# проверить работу метода.

class Road:
    def __init__(self, _length, _width, _weight, _thickness):
        self._length = _length
        self._width = _width
        self._weight = _weight
        self._thickness = _thickness
        
    def get_mass(self):
        print(f'{self._length} м * {self._width} м * {self._weight} кг * {self._thickness} см / 1000') # делим на 1000, тк нужны тонны
        return self._length * self._width * self._weight * self._thickness / 1000
        
r = Road(20, 5000, 25, 5)
print(int(r.get_mass()))

# 3. Реализовать базовый класс Worker (работник):
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
# элементы «оклад» и «премия», например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}
        
class Position(Worker):
    
    def get_full_name(self):
        return f'{self.name} {self.surname}'
        
    def get_total_income(self):
        return f'{self._income} for {self.position}'
        
atr = Position('Ivan', 'Ivanov', 'an ingeneer', '45 000', 'absence')
atr1 = Position('Anna', 'Petrova', 'a photograph', '40 000', '7 000')

print(atr.get_full_name())
print(atr.get_total_income())

print(atr1.get_full_name())
print(atr1.get_total_income())


# Реализуйте базовый класс Car:
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
# также методы: go, stop, turn(direction), которые должны сообщать, что машина
# поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении
# скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
# превышении скорости.


