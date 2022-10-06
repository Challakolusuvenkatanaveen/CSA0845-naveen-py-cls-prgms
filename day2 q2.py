n=int(input("enter the number of elements "))
esum=0
osum=0
l=[]
if(n>0):
    for i in range(n):
        m=int(input("enter the element"))
        l.append(m)
    for i in l:
        if(i%2==0):
            esum=esum+i*i
        else:
            osum=osum+i*i
    print("[",osum,",",esum,"]")
else:
    print("enter the number greater than 0")
