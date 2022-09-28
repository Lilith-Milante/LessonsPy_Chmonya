def input_data ():
    with open('info.csv', 'a', encoding='UTF-8') as f:
        keys = ['name', 'number', 'work']
        values = [i for i in input('Enter name, number and work: ')]
        data_added = dict(zip(keys, values))
        f.write(','.join(data_added))
    return data_added
