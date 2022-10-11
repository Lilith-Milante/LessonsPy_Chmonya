import datetime as dt

# Список в обратном порядке

class ReversedList:

    def __init__(self, list_1):
        self.len_lst = len(list_1)
        self.list_1 = reversed(list_1)

    def __getitem__(self, item):
        return self.list_1[item]

    def __len__(self):
        return self.len_lst

rl = ReversedList([10, 20, 30])
for i in range(len(rl)):
    print(rl[i])

exit()

# Калорийность

class FoodInfo:

    calories = 0

    def __init__(self, proteins, fats, carbohydrates):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    def get_proteins(self):
        return self.proteins

    def get_fats(self):
        return self.fats

    def get_carbohydrates(self):
        return self.carbohydrates

    def get_calories(self):
        print(f'4 * {self.proteins} + 9 * {self.fats} + 4 * {self.carbohydrates}')
        self.calories = 4 * self.proteins + 9 * self.fats + 4 * self.carbohydrates
        return self.calories

    def __add__(self, other):
        return FoodInfo(self.proteins + other.proteins, self.fats + other.fats,\
                        self.carbohydrates + other.carbohydrates)

food1 = FoodInfo(100, 100, 100)
food2 = FoodInfo(50, 60, 70)
food3 = food1 + food2

# print(food1.get_proteins(), food1.get_fats(),\
#       food1.get_carbohydrates(), food1.get_calories())

print(food3.get_proteins(), food3.get_fats(),\
      food3.get_carbohydrates(), food3.get_calories())

# Реализуйте класс Date, экземпляры которого при инициализации принимают месяц и день

class Date:
    def __init__(self, month, day):
        self.month = month
        self.day = day

    def __sub__(self, other):
        day1 = dt.date(2021, self.month, self.day)
        day2 = dt.date(2021, other.month, other.day)
        return str(day2 - day1).split()[0]

day1 = Date(1, 5)
day2 = Date(1, 1)
print(day2 - day1)