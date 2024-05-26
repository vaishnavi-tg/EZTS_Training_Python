def inspect(mystring):
    if len(mystring)%2==0:
        return "Even"
    else:
        return mystring[0]
months=["January","March","May"]
print(list(map(inspect,months))) 






