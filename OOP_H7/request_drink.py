def request(drink_list):
    req = input('Enter drink to find in format - name, volume, price, temperature: \n')
    t = True
    for i in drink_list:
        if req in i:
            print(i)
            t = False
    if t:
        print('This hotdrink is absence -_-')
    return req + f';{not t}'
