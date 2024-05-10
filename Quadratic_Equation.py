input1=int(input())
count=0
for i in range(0,int(input1**0.5)+1):
    for j in range(0,int(input1**0.5)+1):
        for k in range(0,int(input1**0.5)+1):
            if i**2+j**2+k**2+i*j+j*k+k*i==input1:
                count+=1
print(count)                
