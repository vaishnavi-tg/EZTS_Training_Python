# #Imp questions
# 0-100--->Zero---->0
# 100 to 200--->5 rs per Unit
# above 200 it is ---10 rs per Units 
# for 350 units it is 2000


amt=0
nu=int(input("Enter the unit\n"))
if nu<=100:
    amt=0
if nu>100 and nu<=200:
    amt=(nu-100)*5
if nu>200:
    amt=500+(nu-200)*10
print("The amount is",amt)            


 
