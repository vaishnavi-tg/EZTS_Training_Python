# 1 1 4 8 9 27 16 64 25 125 36
n=int(input("Enter the nth term\n"))
if n%2==0:
    print((n//2)**3)
else:
    print(((n+1)//2)**2)    