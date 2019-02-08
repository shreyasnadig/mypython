class fraction:
    def __init__(self,a,b):
        self.num=a
        self.den=b

    def add_frac(self, f2 ):
        f1 = self
	den2 = f1.den * f2.den
        num2 = (f1.num * f2.den) + (f2.num * f1.den)
        sum = fraction ( num2, den2 )
	return ( sum )


def add():
	f1 = fraction ( 1, 2 )
	f2 = fraction ( 2, 3 )
 	print("Given:(f1= )" + str(f1.num) + "/" + str(f1.den) + "+" + "(f2= )" + str(f2.num) + "/" + str(f2.den)) 
	f1 = f1.add_frac(f2 )
	print( "Result: (f1= )" + str(f1.num) + "/" + str(f1.den))

add();
