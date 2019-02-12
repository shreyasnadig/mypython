def str_to_list():
	str = "a=b,c=d,e=f,hello=world"
	print(str)
	ll = str.split(',')
	final_list = []
	for i in range(len(ll)):
		s2= ''.join(ll[i])
		ll2 = s2.split('=')
		final_list.append(tuple(ll2))
	print ( final_list )

str_to_list() 
