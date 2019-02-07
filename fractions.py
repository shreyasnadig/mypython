def gcd(a, b):
    if ( a == 0 ):
        return b;
    return gcd( b % a, a);

def lowest( d3, n3):
    common_factor = gcd(n3, d3);

    d3 = int (d3 / common_factor);
    n3 = int (n3 / common_factor);
    print ( n3, "/", d3);

def addFraction( n1, d1, n2, d2):

    d3=gcd(d1, d2);
    d3=(d1*d2)/d3;

    n3=((n1) * (d3/d1) + (n2) * (d3/d2));

    

    #n1=1; d1=2;
    #n2=2; d2=3;

    print(n1, "/", d1, " + ", n2, "/", d2, " = ", lowest(d3,n3));

addFraction(1,2,2,3);
