g=input("grade=")
n=int(input("enter the salary"))
d=str(n)
if(g=="B"):
    if(n<=0):
        print("enter valid salary")
    else:
        print("salary",n)
        if(n>10000):
            print("bonous",n*10/100)
            print("total to be paid",n+n*10/100)
        else:
            print("bonous",n*2/100+n*10/100)
            print("total",n+n*10/100+n*2/100)
elif(g=="A"):
    if(n<=0):
        print("enter the valid salary")
    else:
        print("salary",n)
        if(n>10000):
            print("bonous",n*5/100)
            print("total",n+n*5/100)
        else:
            print("bonous",n*5/100+n*2/100)
            print("total",n+n*5/100+n*2/100)
else:
    print("enter A  and B grade only")
