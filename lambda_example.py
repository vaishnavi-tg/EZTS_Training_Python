# Using anonymous function
print(lambda a,b:a+b)


#Normal apaproach
def add(a,b):
    return a+b

#Through lambda
print(lambda a,b:a+b)


sum=lambda a,b :a+b
print(sum(2,3))
print(sum(5,9))


sum=lambda a,b :a+b
print(type(sum))
print(sum)