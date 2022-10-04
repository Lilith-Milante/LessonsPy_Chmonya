import random

# 3. Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь, в котором каждый элемент списка
# является и ключом и значением. Предполагается, что элементы списка будут соответствовать правилам задания ключей в словарях.

list_1 = [1, 2, 'third', 'four', 5, 'six', 7]
list_2 = [input() for _ in range(int(input('Enter amount elems: ')))]

def to_dict(lst):
    return {element: element for element in lst} # dict comprehension

print(to_dict(list_1))
print(to_dict(list_2))

# 4. Иван решил создать самый большой словарь в мире. Для этого он придумал функцию biggest_dict(**kwargs), которая принимает
# неограниченное количество параметров «ключ: значение» и обновляет созданный им словарь my_dict, состоящий всего из одного элемента
# «first_one» со значением «we can do it». Воссоздайте эту функцию.

my_dict = {'first_one':'we can do it'}

def biggest_dict (**kwargs):
    my_dict.update(**kwargs)

biggest_dict(second = 2, third = 3, fourth = 4)
print(my_dict)

# 5. Дана строка в виде случайной последовательности чисел от 0 до 9. Требуется создать словарь, который в качестве ключей будет принимать данные числа
# (т. е. ключи будут типом int), а в качестве значений – количество этих чисел в имеющейся последовательности. Для построения словаря создайте функцию count_it(sequence),
# принимающую строку из цифр. Функция должна возвратить словарь из 3-х самых часто встречаемых чисел.

seq_1 = [int(random.randint(0, 5)) for i in range(1, 20)]
print(seq_1)

def count_it (seq_1):
    dict_2 = {int(item):seq_1.count(item) for item in seq_1} # словарь с подсчётом кол-ва встреч.элементов
    sorted_d = sorted(dict_2.items(), key=lambda item: item[1]) # сортируем словарь по значениям
    #sorted_dict = {key: value for key, value in sorted_d}
    return dict(sorted_d[-3:])

print(count_it(seq_1))