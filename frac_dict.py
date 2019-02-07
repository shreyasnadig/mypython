def frac_dict( t1, t2):
    d={}
    d["num"]=t1[1]*t2[1]
    d["den"]=(t1[0]*t2[1]) + (t2[0]*t1[1])
    return d

D=(frac_dict((1,20,(2,3))
print(str(D["num"])+"/"+str(D["den"]))

