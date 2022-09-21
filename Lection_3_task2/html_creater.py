from user_interface import temperature_view
from user_interface import wind_speed_view
from user_interface import preassure_view

def create(device = 1): # например, 1 это для получения значений опред устройства
    style = 'style="font-size:22px;"'
    html = '<html>\n  <head></head>\n <body>\n'
    html += '    <p {}>Temperature: {} c</p>'\
        .format(style, temperature_view(device))
    html += '    <p {}>Wind_speed: {} c</p>' \
        .format(style, wind_speed_view(device))
    html += '    <p {}>Preassure: {} c</p>' \
        .format(style, preassure_view(device))
    html += ' </body>\n</html>'

    with open('index.html', 'w') as page:
        page.write(html)

    return html

def new_create(data, device = 1):
    t, p, w = data
    style = 'style="font-size:22px;"'
    html = '<html>\n  <head></head>\n <body>\n'
    html += '    <p {}>Temperature: {} c</p>'\
        .format(style, t)
    html += '    <p {}>Wind_speed: {} c</p>' \
        .format(style, w)
    html += '    <p {}>Preassure: {} c</p>' \
        .format(style, p)
    html += ' </body>\n</html>'

    with open('new_index.html', 'w') as page:
        page.write(html)

    return data