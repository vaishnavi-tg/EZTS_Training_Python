# input=30
# output=years=0
# week=4
# days=2



# input=20
# output=years=0
# week=2
# days=6


days=int(input("ENter the number of days\n"))
week=days//7
year=days//365
days=days%7
print("Year:",year)
print("Week:",week)
print("days",days)