import csv


def get_data():
    with open('drinks.csv', 'r', encoding='UTF-8') as f:
        reader = csv.reader(f, delimiter=',')
        drinks_list = []
        for row in reader:
            drinks_list.append(row)
            return drinks_list
