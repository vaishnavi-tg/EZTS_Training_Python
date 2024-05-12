mynums=[]
i=1
while i<=5:
    x=int(input("Enter "+str(i)+" element:"))
    mynums.append(x)
    i=i+1
print("The List is :")
sum=0
for x in mynums:
    print(x)
    sum+=x
print("Sum is",sum)        
