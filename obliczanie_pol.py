import math

def get_area(shape): # Dopiero pozniej zajmuje sie ta funkcja

    shape = shape.lower()

    if shape == "rectangle":
        rectangle_area()
    elif shape == "circle":
        circle_area()
    else:
        print("Enter rectangle or circle")

def rectangle_area(): # Tym zajmuje sie jako trzecim
    length = float(input("What is the lenght : "))
    width = float(input("What is the width : "))

    area = length * width

    print("Area of the rectangle is", area)

def circle_area(): # Tym zajmuje sie jako czwartym
    radius = float(input("Enter the radius : "))

    area = math.pi * (math.pow(radius, 2)) # Wykonuje działanie na pole koła

    print("The area of the circle is {:.2f}".format(area))


def main():  # Najpierw zajmowałem się ta funkja

    shape_type = input("Get area for what shape : ")

    get_area(shape_type)





main()
