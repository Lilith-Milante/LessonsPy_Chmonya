# Задайте строку из набора чисел. Напишите программу, которая покажет наименьшее и наибольшее число. В качестве символа-разделителя используйте пробел.

import sympy as sm
import math

a = [int(i) for i in input().split()]
print(max(a), min(a))

# Найдите корни квадратного уравнения Ax² + Bx + C = двумя способами:
# с помощью математических формул, с помощью библиотек Python

a = int(input('Enter A: '))
b = int(input('Enter B: '))
c = int(input('Enter C: '))

D = b**2 - 4*a*c
print(D)

x = 0
x1 = 0
x2 = 0

if D < 0:
    print('Корней нет!')
elif D == 0:
    x = - b / 2 * a
    print(x1)
else:
    x1 = (- b + D ** (1 / 2)) / 2 * a
    x2 = (b + D ** (1 / 2)) / 2 * a
    print(x1, x2)

# var 2

x = sm.Symbol('x')
a = int(input())
b = int(input())
c = int(input())
print(sm.solveset(a * x ** 2 + b * x + c, x))

# Задайте 2 числа. Напишите программу, которая найдёт наименьшее общее кратное этих чисел.

print(sm.lcm(int(input('Enter A ')), int(input('Enter B: '))))

result = math.lcm(int(input('Enter A: '))), int(input('Enter B: '))
print(result)