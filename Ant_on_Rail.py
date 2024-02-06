n=int(input("ENter the total moves of ant"))
arr=list(map(int,input().split()))
c=0
for i in range(n):
    if sum (arr[:i+1])==0:
     c+=1
print(c)    