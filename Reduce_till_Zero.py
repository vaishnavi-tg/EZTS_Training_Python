a=int(input())
b=int(input())
while (b>0):
    if(a<b):
        a,b=b,a
    else:
        a,b=b,a-b
print(a)          