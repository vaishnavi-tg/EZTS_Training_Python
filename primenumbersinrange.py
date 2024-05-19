start=int(input("ENter the start value"))
end=int(input("Enter the end value"))
for i in range(start,end):
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            break
        else:
            print(i,end=' ')