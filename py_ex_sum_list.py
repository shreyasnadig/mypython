def sum_list(l):
	s = 0 #sum variable
	for i in l:
		s = s+i
	return s

def mul_list(l):
	pro = 1
	for i in l:
		pro = pro*i
	return pro


def main():
	#l = [1,2,3,4,5]
	l = input("Enter a list of elements: \n")
	print("Sum: ", sum_list(l))
	print("Product: ", mul_list(l))

if __name__ == '__main__':
	main()

