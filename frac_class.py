class fraction:
    def __init__(self,a,b):
        self.num=a
        self.den=b

    def add_frac( f1,f2 ):
        den2 = f1.den * f2.den
        num2 = (f1.num * f2.den) + (f2.num * f1.den)
        sum = fraction ( num2, den2 )
	return ( sum )

def add():
 f1 = fraction ( 1, 2 )
 f2 = fraction ( 2, 3 )
 f3 = fraction.add_frac( f1,f2 )
 print( str(f3.num) + "/" + str(f3.den))

add();
