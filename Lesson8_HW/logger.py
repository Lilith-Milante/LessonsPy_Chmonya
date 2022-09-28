from datetime import datetime as dt

def log_search(data):
    time = dt.now().strftime('%H:%M') # получили данные по времени (час и минуты)
    with open('log.csv', 'a', encoding='UTF-8') as file:
        file.write('{};\'\Search.. \'\;{}\n'
                   .format(time, data))

def log_added(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a', encoding='UTF-8') as file:
        file.write('{};\'\Added to catalog:\'\;{}\n'
                   .format(time, data))