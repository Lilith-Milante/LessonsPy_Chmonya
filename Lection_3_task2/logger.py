from datetime import datetime as dt

def temperature_logger(data):
    time = dt.now().strftime('%H:%M') # получили данные по времени (час и минуты)
    with open('log.csv', 'a') as file:
        file.write('{};temperature;{}\n'
                   .format(time, data))

def preassure_logger(data):
    time = dt.now().strftime('%H:%M') # получили данные по времени (час и минуты)
    with open('log.csv', 'a') as file:
        file.write('{};preassure;{}\n'
                   .format(time, data))

def wind_speed_logger(data):
    time = dt.now().strftime('%H:%M') # получили данные по времени (час и минуты)
    with open('log.csv', 'a') as file:
        file.write('{};wind_speed;{}\n'
                   .format(time, data))