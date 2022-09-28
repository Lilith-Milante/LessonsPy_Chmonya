def input_data ():
    with open('info.csv', 'a', encoding='UTF-8') as f:
        keys = ['name', 'number', 'work']
        new_user = []
        for item in keys:
            new_user.append(input(f'Enter new user data {item}: '))
        f.write('\n')
        f.write(','.join(new_user))
    return new_user
