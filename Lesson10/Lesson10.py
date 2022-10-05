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