n=int(input("N="))
f=1
count=0
if(n>0):
    for i in range(1,n+1):
        f=f*i
    print(n,"factorial : ",f)
    for j in range(1,n+1):
        if(n%j==0):
            count=count+1
    print("number of factors for ",n,":",count)
else:
    print("enter the number greater than 0")
