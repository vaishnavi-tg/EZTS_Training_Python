num=int(input("Enter the number\n"))
num_str=str(num)
rev=num_str[::-1]
if num_str==rev:
    print("Its a palindrome")
else:
    print("Its not a palindrome")    