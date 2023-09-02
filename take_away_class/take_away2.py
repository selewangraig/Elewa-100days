#Math Operations

import math

print("rectangle, rectangular tank, circle, cylindrical tank")
shape = input("Choose a shape: ")

if shape == "rectangle":
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    perimeter = 2 * (length + width)
    area = length * width
    print("Perimeter:", perimeter)
    print("Area:", area)
elif shape == "rectangular tank":
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    height = float(input("Enter height: "))
    surface_area = 2 * (length * width + length * height + width * height)
    volume = length * width * height
    print("Surface Area:", surface_area)
    print("Volume:", volume)
elif shape == "circle":
    radius = float(input("Enter radius: "))
    circumference = 2 * math.pi * radius
    area = math.pi * radius**2
    print("Circumference:", circumference)
    print("Area:", area)
elif shape == "cylindrical tank":
    radius = float(input("Enter radius: "))
    height = float(input("Enter height: "))
    surface_area = 2 * math.pi * radius * (radius + height)
    volume = math.pi * radius**2 * height
    print("Surface Area:", surface_area)
    print("Volume:", volume)
else:
    print("Invalid shape choice")