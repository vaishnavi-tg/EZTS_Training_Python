arr=list(map(int,input().split()))
n=len(arr)
s=0
d=0
for i in range(n):
    s+=arr[i]
    if abs(s)>d:
        d=abs(s)

print(s)        