def input_data():
    with open('drinks.csv', 'a', encoding='UTF-8') as f:
        keys = ['name', 'volume', 'price', 'temperature']
        new_drink = []
        for item in keys:
            new_drink.append(input(f'Enter new drink {item}: '))
        f.write('\n')
        f.write(','.join(new_drink))
    return new_drink
