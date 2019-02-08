def add_frac(l1,l2):
    den = l1[1] * l2[1]
    num = (l1[0]*l2[1])+ (l2[0]*l1[1])
    return ([num,den])

l3 = add_frac([1,2],[2,3])
print (str(l3[0])+"/"+str(l3[1]))

