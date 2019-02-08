def fib_main(self):
	n=self
	x=0
	y=1
	for i in range (0,n):
		x,y=y,x+y
	return x


print(fib_main(5))
