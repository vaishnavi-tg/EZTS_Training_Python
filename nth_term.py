# 2 3 4 9 8 27 16 81 32 243 64
n=int(input("Enter the nth term\n"))
if n%2==0:
    print(3**(n//2))

else:
    print(2**((n+1)//2))