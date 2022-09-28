def search (user_list):
	req = input('Enter data to find: \n')
	t = True
	for i in user_list:
		if req in i:
			print(i)
			t = False
	if t:
		print('The someone is absence -_-')
	return req + f';{not t}'