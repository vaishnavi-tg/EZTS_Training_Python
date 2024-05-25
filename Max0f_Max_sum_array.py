def max_sum_subarray(arr):
    size=len(arr)
    current_sum=0
    max_so_far=arr[0]
    st=0;end=0;poi=0
    for i in range(0,size):
        current_sum+=arr[i]
        if current_sum>max_so_far:
            max_so_far=current_sum
            st=poi
            end=i
        if current_sum<0:
            current_sum=0
            poi=i+1
    print(max_so_far)            
    print(st)
    print(end)
arr=[4 ,-3, -2 ,2 ,3 ,1, -2, -3, 6 ,-6, -4, 2, 1]
max_sum_subarray(arr)
