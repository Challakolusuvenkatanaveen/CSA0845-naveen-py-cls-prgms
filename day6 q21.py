k=float(input("Enter the number of rows : "))
n=int(k)
if(n>0):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=' ')
        print()
else:
    print("enter the valid number to bulid the pattern")
