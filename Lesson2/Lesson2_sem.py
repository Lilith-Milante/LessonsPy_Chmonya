# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.

n = int(input('Enter n: '))
some_list = []
for i in range(n):
    some_list.append((-3) ** i)
print(*some_list, sep =',') # звёздочка - это распаковка sep - сепаратор, разделитель

# 2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input('Enter n: '))
some_dict = {} # так создаётся словарь
for i in range(1, n + 1):
    some_dict[i] = 3 * i + 1
print(some_dict)

# То же самое, только через функцию

def func(x):
    return 3 * x + 1

n = int(input('Enter n: '))
some_dict = {}
for i in range(1, n + 1):
    some_dict[i] = func(i)
print(some_dict)

# 3. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другую.

str1 = input('Первая строка: ')
str2 = input('Вторая строка: ')
print(str1.lower().count(str2.lower()) or str2.lower().count(str1.lower())) #используем lower, чтобы сделать все буквы маленькими

# то же самое, только сложнее (без функций, вручную)

str1 = input()
str2 = input()
count = 0
if len(str1) < len(str2):
    len_str1 = len(str1)
    i = 0
    while i < len(str2):
        if str1[0] == str2[i]:
            if str1[1:] == str2[i + 1: i + len_str1]:
                count += 1
                i += len_str1
            else:
                i += 1
        else:
            i += 1
print(count)