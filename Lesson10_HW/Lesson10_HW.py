import time

# 1. Создать класс TrafficLight (светофор)

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

exs = TrafficLight('Red', 'Yellow', 'Green')
print(exs.running())

# 2. Реализовать класс Road (дорога)

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
r1 = Road(10, 10, 36, 7)

print(int(r.get_mass()))
print(int(r1.get_mass()))

# 3. Реализовать базовый класс Worker (работник)

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

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def get_name_color(self):
        return f'{self.name} {self.color}'

    def show_speed(self):
        return self.speed

    def go(self):
        print ('An auto grove')

    def stop(self):
        print ('An auto stopped')

    def turn_direction(self):
        if self.is_police: print ('Right turn')
        else: print ('Left turn')

class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            return ('Over speed!')
        else:
            return self.speed

class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            return ('Over speed!')
        else:
            return self.speed

#class PoliceCar(Car):

    # def police_car(self):
    #     if self.is_police: print('Give me your docs')
    #     else: print('Drive calmly')
#class SportCar(Car):

Car1 = TownCar(50, 'Ford', 'Violet', False)
print(Car1.get_name_color())
print(Car1.show_speed())
Car1.go()

Car2 = WorkCar(50, 'Audi', 'Red', True)
print(Car2.get_name_color())
print(Car2.show_speed())
Car2.turn_direction()
Car2.stop()

Car3 = Car(80, 'Toyota', 'Black', False)
print(Car3.get_name_color())
print(Car3.show_speed())
Car3.turn_direction()
Car3.go()
