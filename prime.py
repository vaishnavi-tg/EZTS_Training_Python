num=int(input("Enter the number\n"))
if num==1:
    print("It is not a prime number")
if num>1:
    for i in range(2,int(num/2)):
        if num%i==0:
            print("Its not a prime number")
            break
        else:
            print("Its a prime number")

