# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
import math

day_week = int(input('Enter the day of week: '))
while day_week > 7 or day_week < 1:
    day_week = int(input('The day is not exist! Try enter again: '))
if day_week == 6 or day_week == 7:
    print('This is weekend!')
else:
    print('This is not a weekend')

# 2. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input('Enter X: '))
y = int(input('Enter Y: '))
z = int(input('Enter Z: '))

if not(x or y or z) == (not x) and (not y) and (not z):
    print('True')
else:
    print('False')

# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = float(input('Enter x: '))
y = float(input('Enter y: '))

if x > 0 and y > 0:
    print('1')
if x < 0 and y > 0:
    print('2')
if x < 0 and y < 0:
    print('3')
if x > 0 and y < 0:
    print('4')

if x == 0 and y != 0:
    print('point on the X-asis')
if y == 0 and x != 0:
    print('point on the Y-asis')
if x == 0 and y == 0:
    print('point on the center')

# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarter_num = int(input('Enter quarter number: '))

if quarter_num == 1: print('range of points - x > 0, y > 0')
if quarter_num == 2: print('range of points - x < 0, y > 0')
if quarter_num == 3: print('range of points - x < 0, y < 0')
if quarter_num == 4: print('range of points - x > 0, y < 0')

# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

x1 = float(input('Enter x1: '))
y1 = float(input('Enter y1: '))

x2 = float(input('Enter x2: '))
y2 = float(input('Enter y2: '))

result = float(math.sqrt((x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2)))
print(round(result, 2))