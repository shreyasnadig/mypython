def comp_if ( a, b, c ):
	if((a < b) and (a < c)):
		print (str(a) + " is the smallest")
		#break
	if((b < a) and (b < c)):
		print (str(b) + " is the smallest")
		#break
	if((c < a) and (c < b)):
		print (str(c) + " is the smallest")
		#break

comp_if(3, 1, 2)	
