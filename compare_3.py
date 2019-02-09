def comp_if ( a, b, c ):
	if((a < b) and (a < c)):
		print (str(a) + " is the smallest")
		
	if((b < a) and (b < c)):
		print (str(b) + " is the smallest")
		
	if((c < a) and (c < b)):
		print (str(c) + " is the smallest")
		

def comp_nested_if( a, b, c ):
	if((a < b) and (a < c)):
		print (str(a) + " is the smallest")
	elif(b<c):
		print (str(b) + " is the smallest")
	else:
		print (str(c) + " is the smallest")

def comp_if_eq( a, b, c ):
	low = a if (a < b) else b
	lowest = low if(low < c) else c
	print ( str(lowest) + " is the smallest")


comp_if(3, 1, 2)

comp_nested_if(3, 2, 1)	

comp_if_eq(3, 2, 4)
