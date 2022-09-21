# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

str = input('Enter str: ').replace('абв', '').split(' ')
result = ' '.join(list(filter(lambda x: x != '', str)))
print(result)

# 2. Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока, делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента? - в первый ход нужно взять 20 конфет, поскольку остаток от деления 2021 на 20 будет 1,
# и конфета достанется первому игроку. После каждого хода можно проверять остаток от деления пула на число конфет.

# a) Добавьте игру против бота
# b) Подумайте, как наделить бота "интеллектом"

from random import randint

def enter(name):
    x = int(input(f"{name}, введите количество конфет от 1 до 28: "))
    return x

def p_print(name, k, counter, pull):
    print(f"Ходил {name}, он взял {k}, у него на руках {counter}. Осталось на столе {pull} конфет.")

player1 = input("Enter the name of first player: ")
player2 = input("Enter the name of second player: ")
pull = 2021
who_go = randint(0,2) #жеребьёвка
if who_go:
    print(f"First move {player1}")
else:
    print(f"First move {player2}")

counter1 = 0 # счётчики конфет
counter2 = 0

while pull > 28:
    if who_go:
        k = enter(player1) # сколько ещё забирает
        counter1 += k # сколько у него конфет
        pull -= k # оставшееся кол-во конфет
        who_go = False
        p_print(player1, k, counter1, pull)
    else:
        k = enter(player2)
        counter2 += k
        pull -= k 
        who_go = True
        p_print(player2, k, counter2, pull)

if who_go:
    print(f"{player1} wins!")
else:
    print(f"{player2} wins!")

# если играть против бота, замеcто действий второго игрока, можно прописать выбор рандомного числа из промежутка {0,28}

# 3. Создайте программу для игры в ""Крестики-нолики"".

map = [1, 2, 3, 4, 5, 6, 7, 8, 9] #создаём игровое поле

def print_map():
    print(map[0], end = '|')
    print(map[1], end = '|')
    print(map[2])
    print('-----')
    print(map[3], end = '|')
    print(map[4], end = '|')
    print(map[5])
    print('-----')
    print(map[6], end = '|')
    print(map[7], end = '|')
    print(map[8])

comb = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7],[2,5,7], [1,5,9], [2,4,6]] # это победные комбинации, [,,] - 1 элемент

def enter_pl(enter, symbol): # функция для ввода символа и подмены
    index = map.index(enter)
    map[index] = symbol

def result_check():
    win = '' #запишем сюда победителя
    for i in comb:
        if map[i[0]] == 'X' and map[i[1]] == 'X' and map[i[2]] == 'X': # в каждом элементе comb проверяем, все ли элементы [,,] Х или 0
            win = 'X' and player1_name
        if map[i[0]] == '0' and map[i[1]] == '0' and map[i[2]] == '0':
            win = '0' and player2_name
    return win

player1_name = input("Enter the name of first player: ")
player2_name = input("Enter the name of second player: ")

game_over = False
player1 = True

while game_over == False:
    print_map()

    if player1 == True:
        symbol = 'X'
        enter = int(input(f'{player1_name}, where do you put X? '))
    else:
        symbol = '0'
        enter = int(input(f'{player2_name}, where do you put 0? '))

    enter_pl(enter, symbol) # ход

    win = result_check() # проверка победных комбинаций

    if win != '':
        game_over = True
    else:
        game_over = False
    player1 = not(player1)

print_map()
print(result_check(),'wins!')

# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

with open('start.txt', 'w') as data:
    data.write(input('Enter massage: '))

f = open('start.txt', 'r')
data_2 = f.read()
f.close()

def RLE(data_2):
    res = ''
    count = 1
    for i in range(len(data_2) - 1):
        if data_2[i + 1] == data_2[i]:
            count += 1
        else:
            res += str(count) + data_2[i]
            count = 1
    res += str(count) + data_2[i]
    return res

print(f'Original text: {data_2}')
RLE_res = (RLE(data_2))
print(f'Compressed text: {RLE_res}')

with open('end.txt', 'w') as data_3:
    data_3.write(RLE_res)
