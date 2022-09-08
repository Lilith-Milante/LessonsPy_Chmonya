# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
import random

number = input('Enter real number: ')
sum = 0
for i in number:
    if i != '.':
        sum += int(i)
print(sum)

# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

num_N = int(input('Enter N: '))
mult_step = 1
mult_result = []
for i in range(1, num_N + 1):
    mult_step *= i
    mult_result.append(mult_step)
print(mult_result)

# 3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

def func(n):
    return (1 + 1 / n) ** n

n = int(input('Enter n: '))
dict_seq = {}
for i in range(1, n + 1):
    dict_seq[i] = func(i)
print(dict_seq)
sum_seq = 0
for i in dict_seq:
    sum_seq += int(i)
print(round(sum_seq, 2))

# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input('Enter N: '))
n_list = []
for i in range(n):
    n_list.append(random.randint(-n, n))
print(n_list)  # создали и распечатали лист

mult = open('Positions.txt', 'w')
positions = random.randint(2, n)  # создаёт список позиций элементов, связываем это переменной mult
for i in range(positions):
    mult.write(str(random.randint(1, n - 1)))
    mult.write('\n')
mult.close()

generation = 1
with open('Positions.txt', 'r') as gen:
    for i in gen:
        generation *= n_list[int(i) - 1]
print(f'Произведение элементов на заданных позициях: {generation}')

# 5. Реализуйте алгоритм перемешивания списка.

n = int(input('Enter N: '))
n_list = []
for i in range(n):
    n_list.append(random.randint(-n, n))
print(n_list)

random.shuffle(n_list) # используя команду для перемешивания
print(n_list)

# если алгоритмом

n = int(input('Enter N: '))
n_list = []
for i in range(n):
    n_list.append(random.randint(-n, n))
temp = 0
print(n_list)
for i in range(len(n_list)):
    elem_1 = random.randint(0, len(n_list) - 1)
    elem_2 = random.randint(0, len(n_list) - 1)
    temp = n_list[elem_1]
    n_list[elem_1] = n_list[elem_2]
    n_list[elem_2] = temp
print(n_list)