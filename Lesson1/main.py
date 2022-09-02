# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число:  '))
if first_number ** 2 == second_number or second_number ** 2 == first_number:
    print('да')
else:
    print('нет')

# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

maxx = int(input('Введите число: '))
for i in range(4):
    number = int(input('Введите число: '))
    if number > maxx:
        maxx = number
print(maxx)

# 3. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

n = int(input('Введите N: '))
for i in range(-n, n + 1):
    print(i)

# 4. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

n = float(input("Введите дробное число: "))
result = int(n * 10 % 10)
print(result)

# Можно ещё так:

number = float(input("Введите дробное число: "))
if number // 1 == number:
    print('нет')
else:
    print(int((number * 10 % 10)))

# Или так:

n = input("Введите число: ")
text = n
print(text[2])

# 5. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

n = int(input("Введите число: "))
if ((n % 5 == 0 and n % 10 == 0 or n % 15 == 0) and n % 30 != 0):
    print('Да')
else:
    print('Нет')
