import math
name=input("Enter Your name\n")
first_char=name[:1]
unicode_radius=ord(first_char)
area_circle=math.pi*(unicode_radius**2)
print(area_circle)
