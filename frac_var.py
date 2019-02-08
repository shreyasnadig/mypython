def add_frac(n1,d1,n2,d2):
    num = (n1*d2)+(n2*d1)
    den = d1*d2
    return num,den

n1=1
d1=2
n2=2
d2=3

res = add_frac(n1,d1,n2,d2)
print (str(res[0])+"/"+str(res[1]))


