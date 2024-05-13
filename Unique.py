# [5,6,8,2,3,6,8,5,3]
input1,input2,input3=list(map(int,input().split()))
unique_values=set()
for i in range(input1):
    for j in range(input1):
        remaining_value=input1-i*input2-j*input3
        if remaining_value>0:
            unique_values.add(remaining_value)
print(unique_values)            