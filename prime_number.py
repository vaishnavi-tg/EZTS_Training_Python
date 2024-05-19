num=int(input("Enter the number\n"))
count=0

for i in range(1,num+1):
    if num%i==0:
      count+=1
if count==2:
   print("Its a prime number")
else:
   print("Its not a prime numbera ")      
 