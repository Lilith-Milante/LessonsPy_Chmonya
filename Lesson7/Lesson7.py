# Разделим сервис на этапы:
# Как можно вводить данные?
# ‘Фамилия Имя Номер’
# Как их обрабатывать? Где хранить?
# user = {‘Name’:’’, ‘Last Name’:’’, ‘number’:’’ }
# user_list = [user1,user2,user3……]
# Как запрашивать и получать данные?
# Какие функции можно для этого создать?
# Как вынести функции в модули?


# Иванов Иван +712345
# Семенов Семен +734567
# Матвеев Матвей +756789
# Сидоров Дмитрий +712377
# Григорьев Станислав +799875

def txt_input(rad):
	f = open('data.txt', 'r', encoding="utf-8")
	num = f.readlines()
	lst_dict = []
	for i in num:
		raw_test = i.split()
		user_data = { 'LastName': raw_test[0],'Name': raw_test[1], 'Number': raw_test[2]}
		lst_dict.append(user_data)
	f.close()
	return lst_dict

r = 'data.txt'
print(txt_input(r))

def search(lst):

request = input('?: ')
user_list = [{'LastName': 'Семенов', 'Name': 'Семен', 'Number': '+734567'}, {'LastName': 'Матвеев', 'Name': 'Матвей', 'Number': '+756789'}, {'LastName': 'Сидоров', 'Name': 'Дмитрий', 'Number': '+712377'}, {'LastName': 'Григорьев', 'Name': 'Станислав', 'Number': '+79987'}]
t = True
for i in user_list:
if i['LastName'] == request or i['Name'] == request or i['Number'] == request:
	print(*i.values())
	t = False
if t:
print('Нет такого usera')

