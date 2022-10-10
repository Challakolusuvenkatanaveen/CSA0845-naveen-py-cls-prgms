k=float(input("Enter the number of rows : "))
n=int(k)
m=1
if(n>0):
    for i in range(n+1):
        for j in range(i):
            print(m,end=' ')
            m=m+1
        print()
else:
    print("enter the valid number to bulid the pattern")
