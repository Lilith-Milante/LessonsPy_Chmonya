class Auto:

    auto_count = 0
    def __init__(self, auto_name, auto_model):
        self.auto_name = auto_name
        self.auto_model = auto_model
        Auto.auto_count += 1
        print(self.auto_name, self.auto_model)
        print(Auto.auto_count)

a = Auto('BMW', 'M5')
print(a.auto_name)

# Напишите класс LittleBell, который при вызове метода sound печатает слово 'ding'

class LittleBell:

    def sound(self):
        print('ding')

bell = LittleBell()
bell.sound()
bell.sound()
bell.sound()

# Напишите класс кнопки Button, экземпляры которого будут измерять количество нажатий на кнопку-объект.
# метод click увеличивает количество нажатий, метод ckick_count возвращает число нажатий. Метод reset обнуляет количество нажатий.

class Button:
    count = 0

    def click(self):
        Button.count += 1

    def click_count(self):
        return Button.count

    def reset(self):
        Button.count = 0

button = Button()
button.click()
button.click()
print(button.click_count())
button.reset()
button.click()
print(button.click_count())

# Напишите класс Balance для описания весов с двумя чашами.
# метод add_right принимает целое число - вес, положенный на правую чашу весов, add_left - на левую чашу.
# метод result должен возвращать символ =, если вес на чашах одинаковый, R если правая, L - если левая

class Balance:

    def __init__(self):
        self.right_count = 0
        self.left_count = 0

    def add_right(self, right):
        self.right_count += right

    def add_left(self, left):
        self.left_count += left

    def result(self):
        if self.right_count > self.left_count:
            print('R')
        elif self.right_count < self.left_count:
            print('L')
        elif self.right_count == self.left_count:
            print('=')

balance = Balance()
balance.add_right(10)
balance.add_left(9)
balance.add_left(2)
balance.result()
balance.add_left(1)
balance.result()

# Напишите класс BigBell, который при вызове метода sound печатает попеременно слова ding и dong, начиная с ding.

class BigBell:

    def __init__(self):
        self.num = 0

    def sound(self):
        if self.num == 0:
            print('ding')
            self.num = 1
        else:
            print('dong')
            self.num = 0

bell = BigBell()
bell.sound()
bell.sound()
bell.sound()

# либо

class BigBell:

    def __init(self):
        self.count = True

    def click(self):
        if self.count:
            print('ding')
        else:
            print('dong')
        self.count = not self.count

bell = BigBell()
bell.click()
bell.click()
bell.click()

# Напишите класс OddEvenSeparator, в который можно добавлять числа, получая потом отдельно чётные или нечётные.
# Добаление с помощью метода add_number. Методы even и odd должны возвращать списки чётных и нечётных чисел.

class OddEvenSeparator:

    def __init__(self):
     self.some_list =[]

    def add_number(self, num):
        self.some_list.append(num)

    def even(self):
        return list(filter(lambda x: not x % 2, self.some_list))

    def odd(self):
     return list(filter(lambda x: x % 2, self.some_list))

separator = OddEvenSeparator()
separator.add_number(1)
separator.add_number(5)
separator.add_number(6)
separator.add_number(8)
separator.add_number(3)
print(" ".join(map(str, separator.even())))
print(" ".join(map(str, separator.odd())))

# Напишите класс MinMaxWordFinder. Класс должен уметь анализировать текст и находить в нём слова наименьшей и наибольшей длины.
# Текст состоит из предложений, которые добавляются методом sentence. Метод shortest_words возвращает список самых коротких слов, метод -
# longest_words - самых длинных. Слова, отсортир. методами, должны быть по алфавиту.

class MinMaxWordFinder:

    def __init__(self):
        self.some_list = []

    def add_sentence(self, text: str):
        for word in text.split():
            self.some_list.append(word)

    def shortest_words(self):
        return [x for x in self.some_list if len(x) == min(map(len, self.some_list))]

    def longest_words(self):
        return [x for x in self.some_list if len(x) == max(map(len, self.some_list))]

finder = MinMaxWordFinder()
finder.add_sentence('hello abc world')
finder.add_sentence("def asdf qwert")
print(' '.join(finder.shortest_words()))
print(' '.join(finder.longest_words()))