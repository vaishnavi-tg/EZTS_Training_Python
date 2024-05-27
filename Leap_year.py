year=int(input("Enter the year\n"))
if year%4==0:
    if year%400==0 or year%100!=0:
        print("Its a leap year")
    else:
        print("Its not a leap year")        
