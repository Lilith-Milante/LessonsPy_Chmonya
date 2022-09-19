# 1. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +, -, /, *.приоритет операций стандартный.
#*Пример: *
# 2 + 2 = > 4;
#
# 1 + 2 * 3 = > 7;
#
# 1 - 2 * 3 = > -5;

symbol = {}
result = 0
str =''
str = input('Введите строку с формулой: ').split()
i = 0
while len(str) != 1:
    if str[i] == '*':
        index = str.index('*')
        str[index] = int(str[index-1]) * int(str[index+1])
        str.remove(str[index-1])
        str.remove(str[index])
        i = 0
        #print(str)
    elif str[i] == '/':
        index = str.index('/')
        str[index] = int(str[index - 1]) / int(str[index + 1])
        str.remove(str[index - 1])
        str.remove(str[index])
        i = 0
        #print(str)
    i += 1

print(str)

formula = [i for i in input('Введите строку: ').split()]
i = 0
while i < len(formula) - 1:
    if formula[i] == '*':
        index = formula.index('*')
        formula[index] = int(formula[index - 1]) * int(formula[index + 1])
        formula.pop(index - 1)
        formula.pop(index)
        print(formula)
        i = 0
    elif formula[i] == '/':
        index = formula.index('/')
        formula[index] = int(formula[index - 1]) // int(formula[index + 1])
        formula.pop(index - 1)
        formula.pop(index)
        print(formula)
        i = 0
    i += 1

i = 0
while len(formula) > 1:
    if formula[i] == '+':
        index = formula.index('+')
        formula[index] = int(formula[index - 1]) + int(formula[index + 1])
        formula.pop(index - 1)
        formula.pop(index)
        print(formula)
        i = 0
    elif formula[i] == '-':
        index = formula.index('-')
        formula[index] = int(formula[index - 1]) - int(formula[index + 1])
        formula.pop(index - 1)
        formula.pop(index)
        print(formula)
        i = 0
    i += 1

print(formula)

# 2. Дана последовательность чисел.Получить список уникальных элементов заданной последовательности.
#*Пример: [1, 2, 3, 5, 1, 5, 3, 10] = > [2, 10]
