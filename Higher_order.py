#Map and filter functions
# eg=r=map(func,iterable)


def square(num):
    return num**2
mynums=[1,2,3,4,5]
for x in mynums:
    print(square(x))




def square(num):
    return num**2
mynums=[1,2,3,4,5]
result=map(square,mynums)
print(result)   