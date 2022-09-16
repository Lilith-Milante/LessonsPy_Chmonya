# def f(x):
#     return x**2
#
# g = f # кладём функцию в переменную, пременная хранит ссылку на функцию
# print(type(f))
# print(type(g))
#
# print(f(2))
# print(g(2))

# def calc(x):
#     return x + 10
#
# print(calc(10))

# def calc2(x):
#     return x * 10
#
# print(calc2(10))
#
# def math(op, x): op - opetation операция
#     print(op(x))
#
# math(calc2, 10) # 100

def sum(x,y):
    return x+y


def mult(x,y):
    return x*y

def calc(op, a, b):
    print(op(a, b))
    #return(op(a, b))

calc(mult, 4, 5) # взяли и написали функцию которая обращается к функции mult
# получили 20

calc(sum, 4, 5) # обращаемся к функции и передаём аргументы
sum = lambda x, y: x+y # ввели переменную, которая делает то же самое, что и функция sum
calc(lambda x, y: x+y, 4, 5) # вызвали переменную, которая выполняет действие функции

# List Comprehension - быстрое создание списков

# list = []
#
# for i in range(1, 101):
#     #if(i % 2 == 0):
#         list.append(i)

list1 = [i for i in range(1, 21) if i % 2 == 0] # то же, что и выше, но в другом виде
list2 = [(i,i) for i in range(1, 21) if i % 2 == 0] # i, i - как получить список кортежей
# первый арг - что хотим получить, из чего и по какому условию

def f(x):
    return x**3

list3 = [f(i) for i in range(1, 21) if i % 2 == 0] # для каждого чётного элемента из диапазона будет применяться функция выше
print(list3)
list4 = [((i),f(i)) for i in range(1, 21) if i % 2 == 0] # создали пары число-куб (кортежи)
print(list4)

# задача: из списка 5 выбрать чётные числа и вывести в паре (число, квадрат числа)

def f(x):
    return x**2

list5 = [1, 2, 3, 5, 8, 15, 23, 38]
list6 = [(i, f(i)) for i in list5 if i % 2 == 0]
print(list6)

# считаем данные с файла

# path = '\Курс Разработчик\II Четверть\01 Знакомство с языком Python\Семинары\LessonsPy_Chmonya\Lec2.txt'
# f = open(path, 'r')
# data = f.read() + ' ' # считываем данные оттуда и добавл пробел
# f.close()
#
# list7 = []
#
# while data != '':
#     space_pos = data.index(' ') # ищем первую позицию пробела
#     list7.append(int(data[:space_pos])) # берём всё, что находится от первого символа до позиции первого пробела
#     data = data[space_pos+1:] # обновляем нашу строку
#
# out = []
# for e in list7:
#     if not e % 2:
#         out.append((e, e**2))
# print(out)

#

def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

data = '1 2 3 4 8 15 23 38'.split()

res = map(int, data)
res = filter(lambda x: not x % 2, res)
res = list(map(lambda x:(x, x**2), res))
print(res)

# map - показываем функцию и то, куда хотим применить

list8 = [x for x in range(1, 20)]

list8 = list(map(lambda x:x+10, list8))

print(list8)

data1 =  list(map(int, input().split()))
print(data1)

# filter - функция, этер объект, - применяем функ к каждому элементу

data = [x for x in range(10)]
res = (filter(lambda x: not x % 2, data))
print(res)

# zip

users = ['user1', 'user2', 'user3']
ids = [4,6,9]

data2 = list(zip(users, ids))
print(data2)

# enumerate

data2 = list(enumerate(users))
print(data2)