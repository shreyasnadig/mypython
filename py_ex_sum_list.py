def sum_list(l):
	s = 0; #sum variable
	for i in l:
		s = s+i
	return s

def main():
	#l = [1,2,3,4,5]
	l = input("Enter a lost of elements: \n")
	print(sum_list(l))

if __name__ == '__main__':
	main()

