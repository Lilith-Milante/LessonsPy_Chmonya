# найти элменты, начинающиеся на i
products = ['iPad', 'Samsung Galaxy', 'iPhone', 'iRiver']


def isFirstI(elem):
    return elem[0] == "i"


resultList = list(filter(isFirstI, products))
print(resultList)
#
# products = ['iPad', 'Samsung Galaxy', 'iPhone', 'iRiver']
# new_list = list(lambda(x: x[0] == 'i', products))
# print(new_list)
#
#
# products = ['iPad', 'Samsung Galaxy', 'iPhone', 'iRiver']

#
def f(str):
    if str[0] == "i":
        return str

print(list(filter(f, products)))

# есть список с ценами на товары (тип данных — str ), получить из него
# кортеж с ценами (тип данных — float )

prices = ['1578.4', '892.4', '354.1', '871.5']

cort = tuple(map(float, prices))

print(cort)

# применить скидку к товарам и округлить до 2 знака

DISCOUNT = 7
prices = ['1578.4', '892.4', '354.1', '871.5']

pricesNew = list(map(lambda x: x*(100 - DISCOUNT)/100, prices))
print(pricesNew)
#
# 35. Есть N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 == A[i-1]. Найдите это число.
# 	my_str = ‘1 2 3 5 6’ => 4
# 36. Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 5, 6, 7]
#
# 37. Напишите программу, удаляющую из текста все слова, содержащие "абв".
