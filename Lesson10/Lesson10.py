# class Auto:
# # атрибуты класса
# auto_count = 0
# # методы класса
# def __init__(self, auto_name, auto_model):
# self.auto_name = auto_name
# self.auto_model = auto_model
# Auto.auto_count += 1
# print(self.auto_name, self.auto_model)
# print(Auto.auto_count)
#
# a = Auto('BMW', 'M5')
# print(a.auto_name)

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

# class OddEvenSeparator:

# def __init__(self) -> None:
# self.some_list =[]


# def add_number(self, num):
# self.some_list.append(num)

# def even(self):
# return list(filter(lambda x: not x%2, self.some_list ))

# def odd(self):
# return list(filter(lambda x: x%2, self.some_list ))

# separator = OddEvenSeparator()
# separator.add_number(1)
# separator.add_number(5)
# separator.add_number(6)
# separator.add_number(8)
# separator.add_number(3)
# print(" ".join(map(str, separator.even())))
# print(" ".join(map(str, separator.odd())))

class MinMaxWordFinder:

    def __init__(self) -> None:
        self.some_list =[]

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