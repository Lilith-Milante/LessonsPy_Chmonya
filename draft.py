# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:  - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

k = int(input('Enter degree k: '))
list_3 = []
for i in range(k):
    list_3.append(random.randint(0, 100)) # коэффициенты
print(list_3)

def polynomial(k):
    plnm = ''
    for i in list_3:
        if i == 0:
            plnm += ''
        elif i == 1:
            plnm = str(f'x ** {len(list_3)} + ')
        elif len(list_3) != 1:
            plnm = str(f'{i} * x ** {len(list_3)} + {i} x ** {len(list_3) - 1}')
        else:
            plnm = str(f'{i} * x ')
    l = random.randint(0, 100)
    if l != 0:
        plnm += str(f' + {l} = 0')
    else:
        plnm += str(f' = 0')
    print(plnm)

plmn = polynomial(k)
print(plmn)

with open('Result.txt', 'w') as result:
    result.write(str(plmn))