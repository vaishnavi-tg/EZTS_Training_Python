# Write a function called find_largest() which accepts
# multiple strings as arguments and returns the length 
# of the largest string
def find_largest(*names):
    max=0
    for s in names:
        if len(s)>max:
            max=len(s)
    return max        
print(find_largest("January","February","March"))

print("---Return the largest string only---")
def find_largest(*names):
    max=0
    largest=''
    for s in names:
        if len(s)>max:
            max=len(s)
            largest=s
    return largest        
print(find_largest("January","February","March"))