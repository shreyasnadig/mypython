def fib():
	a,b=0,1
	while True:
		yield a
		a,b=b,a+b
j = 15
x = fib()
for i in x and j in range(10,0,-1):
	#if(not j):
	#	break
	print(i)
