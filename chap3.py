#Excercise1d

def pay(hours, rate):
	if( hours > 40 ):
		hours = hours-40
		rate = rate * 1.5
		return (400+hours*rate)
	return (hours*rate)

def main():
	try:
		hours = input("Enter Hours: ")
		h = float(hours)
		rate = input("Enter Rate: ")
		r = float(rate)
		p = pay( h , r )
		print 'Pay: ', p
	except:
		print("Error, please enter a numeric value")
		 

if __name__ == '__main__':
	main()

