import csv

def get_data():

    with open('info.csv', 'r', encoding='UTF-8') as f:
        reader = csv.DictReader(f, delimiter=',')
        user_list = []
        for row in reader:
            user_list.append(row)
        return user_list