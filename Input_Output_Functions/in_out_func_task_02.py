#Write a python program that wil prompt the user
#to perform calculations of Area, Surface Area and volume of a cuboid
#using the formulae:
#Area = length * width
#Surface Area = 2(length * width) + 2(length * height) + 2(width * height)
#Volume = length * width * height


#function to prompt user input
def cuboid():
    global length, width, height
    length = float(input("Enter length of Cuboid: "))
    width = float(input("Enter width of Cuboid: "))
    height = float(input("Enter height of Cuboid: "))

    return length, width, height

#function to calculate area
def area_cuboid():
    global length, width
    area = length * width
    print(f"\nThe area of the cuboid is: {area}")

#function to calculate surface area
def surf_area_cuboid():
    global length, width, height
    surf_area = (2 * (length * width)) + (2 * (length * height)) + (2 * (height * width))
    print(f"The surface area of the cuboid is: {surf_area}")

#function to calculate volume
def vol_cuboid():
    global length, width, height
    vol = length * width * height
    print(f"The volume of the cuboid is: {vol}")

#function call
cuboid()
area_cuboid()
surf_area_cuboid()
vol_cuboid()
