from urllib import request

def info_input():
	with open('data.csv', 'r', encoding="UTF-8") as f:
	names = f.readlines()
	lst_dict = []
	for i in names:
		raw_test = i.split()
		user_data = { 'LastName': raw_test[0],'Name': raw_test[1], 'Number': raw_test[2]}
		lst_dict.append(user_data)
	return lst_dict

print(lsi_dict)

exit()

def search (user_list):
	request = input('?: ')
	user_list = [{'LastName':'Семенов', 'Name':'Семен', 'Number':'+734567'},
				 {'LastName':'Матвеев', 'Name':'Матвей', 'Number':'+756789'},
				 {'LastName':'Сидоров', 'Name':'Дмитрий', 'Number':'+712377'},
				 {'LastName':'Григорьев', 'Name':'Станислав', 'Number':'+79987'}]


t = True
for i in user_list:
	if i['LastName'] == request or i['Name'] == request or i['Number'] == request:
		print(*i.values())
t = False
if t:
	print('Нет такого usera')

search(user_list)

print(info_input(r))
