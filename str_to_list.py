def str_to_list(st):
	str = st
	print(str)
	ll = str.split(';')
	final_list = []
	for i in range(len(ll)):
		s2= ''.join(ll[i])
		ll2 = s2.split('=')
		final_list.append(tuple(ll2))
	print ( final_list )

def main():
	s = input("Enter a string:")
	str_to_list(s)

if __name__ == '__main__':
	main()
