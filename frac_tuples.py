def add_frac( t1, t2):
    den = t1[1] * t2[1]
    num = (t1[0] * t2[1]) + (t2[0] * t1[1])
    return (num,den)

t3 = add_frac((1,2),(2,3))
print (str(t3[0])+"/"+str(t3[1]))


    
