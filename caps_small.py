# APPROACH 1
alpha=input("Enter the alphabet\n")
if("A"<=alpha<="Z"):
    print("Its a capital letter")
else:
    print("Its a small letter")  




alpha=input("Enter the alphabet\n")
b=ord(alpha)
if(chr(65)<=chr(b)<=chr(90)):
    print("Its a capital letter")
else:
    print("Its a small letter")       