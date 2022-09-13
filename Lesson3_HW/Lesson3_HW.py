# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

list_1 = [6, 7, 1, -8, 4, 5, -2]
print(list_1)
sum = 0
for i in range(0, len(list_1), 2):  # индекс первого элемента, последнего и шаг
    sum += list_1[i]
print(sum)

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

list_2 = [-8, 5, 1, -5, -6, 0, 1, -3]
print(list_2)
list_3 = []
for i in range(int(len(list_2) / 2)):
    list_3.append(list_2[i] * list_2[len(list_2) - i - 1])
print(list_3)

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

list_4_float = [1.35, 6.87, 4.5, -3.21, -8.7]
print(list_4_float)
list_5 = []
for i in list_4_float:
    list_5.append(i % 1 * 100)  # добавляет остаток от деления на 1, то есть дробную часть
print(list_5)

for i in list_5:
    mx = list_5[0]
    if i > mx:
        mx = i

for i in list_5:
    mn = list_5[0]
    if i < mn:
        mn = i
print(round(mx - mn), '\t')

# можно не искать max и min вручную

list_4_float = [1.35, 6.87, 4.5, -3.21, -8.7]
print(list_4_float)
list_5 = []
for i in list_4_float:
    list_5.append(i % 1 * 100) # добавляет остаток от деления на 1, то есть дробную часть

print(list_5)
print(round(max(list_5) - min(list_5)), '\t')

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

num_dec = int(input('Enter the number dec: '))

def bin(num_dec):
    num_bin = " "
    while num_dec != 0:
        num_bin += str(num_dec % 2)
        num_dec //= 2
    return ''.join(reversed(num_bin))
print(bin(num_dec))

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# если k = 8, то [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

num = int(input('Enter the number: '))

def fibonacci_nums(num):
    f_nums = []
    num_1, num_2 = 1, 1
    for i in range(num):
        f_nums.append(num_1)
        num_1, num_2 = num_2, num_1 + num_2

    num_1, num_2 = 0, 1
    for i in range (num + 1):
        f_nums.insert(0, num_1)
        num_1, num_2 = num_2, num_1 - num_2
    return f_nums

print(fibonacci_nums(num))