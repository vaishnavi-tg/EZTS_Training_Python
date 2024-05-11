string=input("Enter the string\n")
count=0
for i in string:
    if i==" ":
       count+=1
print("The total number of space in the given string is",count)

print('-------------------------')



# Solution of sir

s=input("Enter the string\n").split()
print(len(s)-1,"Is the number of spaces in the entered string")
   