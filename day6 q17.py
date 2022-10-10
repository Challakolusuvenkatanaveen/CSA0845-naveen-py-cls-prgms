n=int(input("N="))
if(n>=0):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)
else:
    print("enter the valid input")
