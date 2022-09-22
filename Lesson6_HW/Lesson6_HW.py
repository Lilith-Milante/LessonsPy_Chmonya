# 1. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +, -, /, *.приоритет операций стандартный.
#*Пример: *
# 2 + 2 = > 4;
#
# 1 + 2 * 3 = > 7;
#
# 1 - 2 * 3 = > -5;

list_1 = [i for i in input('Enter formula: ').split()]

def calc(list_1):
    while len(list_1) > 1:
        if list_1.count('*') != 0:
            index = list_1.index('*')
            list_1[index] = int(list_1[index - 1]) * int(list_1[index + 1])
            list_1.pop(index - 1)
            list_1.pop(index)

        elif list_1.count('/') != 0:
            index = list_1.index('/')
            list_1[index] = int(list_1[index - 1]) / int(list_1[index + 1])
            list_1.pop(index - 1)
            list_1.pop(index)

        elif list_1.count('-') != 0:
            index = list_1.index('-')
            list_1[index] = int(list_1[index - 1]) - int(list_1[index + 1])
            list_1.pop(index - 1)
            list_1.pop(index)

        elif list_1.count('+') != 0:
            index = list_1.index('+')
            list_1[index] = int(list_1[index - 1]) + int(list_1[index + 1])
            list_1.pop(index - 1)
            list_1.pop(index)

# 2. Дана последовательность чисел.Получить список уникальных элементов заданной последовательности.
#*Пример: [1, 2, 3, 5, 1, 5, 3, 10] = > [2, 10]

list_2 = [i for i in input('Enter numbers: ').split()]

def delete_num(args):
    once = [i for i in args if args.count(i) == 1]
    return once

print(list_2)
print(delete_num(list_2))
