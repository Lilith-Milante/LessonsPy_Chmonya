# 1. Вычислить число c заданной точностью d.
import math
import random

n = float(input('Enter n: '))
d = float(input('Enter d (10\u207B\u00B9; 10\u207B\u00B9\u2070): ')) # выводим степени кодировкой

s = str(d)
#print(abs(s.find('.') - len(s)) - 1)
f = abs(s.find('.') - len(s) - 1) # находим число знаков после запятой
print(round(n, f))
def num_d(n, d):
    return (n // d) * d

res = num_d(n, d)
print(res)
#

d = str(input('Введите значение d в условии (10^(-1) <= d <= 10^(-10): '))
d = int(len(d) - 2)
for i in range(int(len(d))):
    i != '.'
res = round(n, i)

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

nm = int(input('Enter n: '))
m = 2  # делим число нацело как первый шаг
list_1 = []
while nm > 1:
    if nm % m == 0:
        list_1.append(m)
        nm /= m  # nm = nm / m - получаем от частного новое число для деления
    else:
        m += 1  # увеличиваем m чтобы перейти к искомому множителю
print(list_1)

# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

list_2 = [int(i) for i in input().split()]
print(list_2)
print(set(list_2))  # преобразуем лист во множество

# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:  - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

k = int(input("Enter degree k: "))

def polynomial(k):
    s = ''
    r = 0
    for i in range(k): # степени
        r = random.randint(0, 100) # генерация коэффициентов
        if r == 0:
            s += ''
        elif r == 1:
            s += str(f'x^{i} + ')
        elif i != 1:
            s += str(f'{r}x^{i} + ')
        else:
            s += str(f'{r}x ')
    r = random.randint(0, 100) # генерация свободного коэффициента
    if r != 0:
        s += str(f'+ {r} = 0')
    else:
        s += str(f'= 0')
    return s

plmn = (polynomial(k))
print(plmn)

with open('Result.txt', 'w') as result:
    result.write(plmn)

# 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
