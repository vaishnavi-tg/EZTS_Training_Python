n=int(input())
arr=list(map(int,input().split()))
arr.sort()
m1,m2=arr[-1],arr[-2]
av=(m1+m2)/2
s=0
for i in range(len(arr)):
    if arr[i]>=av:
        s=s+arr[i]
print(s)        
