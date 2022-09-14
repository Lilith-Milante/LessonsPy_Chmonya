# Работа с файлами
# Завести переменную, которая будет связана с файлом, указать путь к файлу, в каком режиме будем работать с файлом
# a - открытие с добавлением, r - открытие для чтения, w - открытие для записи

exit()  # позволяет не выполнять код, который прописан дальше

list = ['one', 'two', 'tree11']
data = open('example.txt', 'w')  # присвоили переменной файл и указали путь, выбрали режим работы
data.writelines(list)  # передали данные нашего списка в эту переменную, обязательно должен быть текст
data.write('list\n')
data.write('list\n')  # передаёт данные, делаем отступ
data.close()  # закрыли файл

# либо так: в данном случае файл закрывается сам

with open('example.txt', 'w') as list:  # прописали открытие и обозначили переменную
    data.write('list\n')
    data.write('list\n')

# чтение
path = 'example.txt'
data = open(path, 'r')  # открыли в режиме чтения
for line in data:
    print(line)
data.close()

# функции
print(sum([int(i) for i in input() if i != '.']))
#

import example as ex

#
print(ex.f(1))


def concatenatio(*params):  # пример функции, в выводе там её вызываем и передаём параметры
    result: str = ''  # тут пописываем тип данных, можно прописать и инт или вообще не писать
    for item in params:
        result += item
        return result


print(concatenatio('a', 'b', 'c', '5'))


# рекурсия на примере чисел Фибоначчи

def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


list = []
for e in range(1, 10):
    list.append(fib(e))
print(list)

# кортежи (tuple) - неизменяемые списки, как в листах есть индексы, можно ссылаться на них

a = (3, 4, 3, 6, 8)
print(a[-2])  # 6
for item in a:
    print(item)

t = tuple(['one', 'two', 'tree'])
one, two, tree = t
print = ('o:{}, t:{}, t:{}'.format(one, two, tree))

# словари - коллекции с доступом к елементам по ключу

dictionary = {}  # создали пустой словарь
dict = \
    {
        'one' : '1',
        'two' : '2',
        'tree' : '3',
        'four' : '4'
    }

print(dict)
print(dict['two'])

for k in dict.keys(): #как напечатать все ключи, если укажем values, то по значениям
    print(k)

# множества

numbers = {'one', 'two', 'tree'}
print(numbers)
numbers.add('four')
print(numbers)
numbers.remove('one')
print(numbers)
numbers.clear()

s = frozenset(a) # замороженное множество, неизменяемое

#списки

list_1 = [1,2,3,4]

print(list_1.pop(2)) # удаляет указанный элемент по его индексу, если пустые скобки, удаляет последний
print(list_1)

print(list_1.insert(2,5)) # число какое хотим вставить и на какую позицию
print(list_1)

print(list_1.append(11)) # добавление элемента в конец
print(list_1)

from decimal import Decimal
print(Decimal(str(нужноечисло)).as_tuple().exponent*(-1)) - узнать кол-во знаков после запятой