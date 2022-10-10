n=int(input("A="))
b=int(input("B="))
if(n>0 and b>0):
    if(n==b or n>b):
        print(" cant printthe composite number because no numbers between")
    else:
        for i in range(n+1,b):
            count=0
            for j in range(1,i+1):
                if(i%j==0):
                    count=count+1
            if(count!=2):
                print(i)

else:
    print("enter the valid input")
