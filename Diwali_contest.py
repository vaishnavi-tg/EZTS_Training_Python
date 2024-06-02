'''8pm to 12 am---->4hr--->240 m
home to party--->180
solving--->i*5
240-180--->60-5
55-10=45
45-15=30
30-20=10
10-25='''


n=int(input())
p=int(input())
x=240-p
c=0
for i in range(1,n+1):
    if x>0 and x>i*5:
        x=x-(i*5)
        c=c+1
    else:
        break
print(c)        
