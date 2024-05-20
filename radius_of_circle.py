def cal_area(radius,pi=3.142):
    area=pi*radius*radius
    return area
num=int(input("Enter the radius of the circle\n"))
print(cal_area(num))
