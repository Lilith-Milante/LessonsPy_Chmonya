# 1. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.


# Требуемый диапазон [50, 100) -> случайное число 12353 ->ширина диапазона 100-50=50 -> seed%50 <=> seed%(upper-lower) [0,49]-> сдвигаем на 50 -> [50, 99]

# 2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

lst = [str(i) for i in input('Введите значения списка через пробел: ').split()]
num = input('некое число: ')
for i in lst:
     if i == num:
         print(i)
     else:
         print('нет')
print('lst')

# 3. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

lst = [str(i) for i in input('Введите значения списка через пробел: ').split()]
num = input('некая строка: ')
count_1 = 0
count_2 = 0
for i in lst:
    if num == i:
        count_1 += 1
        if count_1 == 2:
            print(count_2)
            break
    count_2 += 1
else:
    print('Нет')

some_list = [input() for _ in range(int(input('Введите кол-во элементов: ')))]
some_str = input('Введите строку: ')
try:
    print(some_list.index(some_str, some_list.index(some_str) + 1))
except:
    print(-1)

some_list = [input() for _ in range(int(input('Введите кол-во элементов: ')))]
some_str = input('Введите строку: ')
start = some_list.index(some_str) + 1
try:
    print(some_list.index(some_str, start, -1))
except:
    print(-1)