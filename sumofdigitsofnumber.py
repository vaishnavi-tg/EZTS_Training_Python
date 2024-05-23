num=int(input("Enter the number\n"))
rem=0
digit=0
while num>0:
    digit=num%10
    rem=rem+digit
    num=num//10
print(rem)    
