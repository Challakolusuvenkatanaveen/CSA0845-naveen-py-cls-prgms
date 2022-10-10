n=float(input("Enter the age"))
if(n>0):
    if(n>18):
        print("eligible for vote")
    else:
        print("not eligible\nrequired age ",18-n)
else:
    print("enter the valid age")
    
