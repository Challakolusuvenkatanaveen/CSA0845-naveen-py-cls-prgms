n=int(input("enter the number "))
j=[]
for u in range(n):
    m=int(input(""))
    j.append(m)
print(j)
sum=0
for i in range(n):
    if(j[i]<j[i+1]):
        l=j[i+1]-j[i]
        sum=sum+l
print(l)
