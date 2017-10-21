import math


def get_area(shape): # Nastepnie zajmuje sie tym

    shape = shape.lower()

    if shape == "prostokat":
        prostokat_area()

    elif shape == "kwadrat":
        kwadrat_area()

    elif shape == "kolo":
        kolo_area()


    else:
        print("You must pick kwadrat or prostokąt")


def prostokat_area():

    dlugosc = float(input("Enter length : "))
    szerokosc = float(input("Enter width : "))

    area = dlugosc * szerokosc

    print("Area of the prostokat is :", area)



def kwadrat_area():

    dlugosc_boku = float(input("Enter length : "))

    area = dlugosc_boku **2

    print("Area of the square is :", area)

def kolo_area():
    promien = float(input("Ener the radius : "))

    area = math.pi * (promien **2)

    print("Area of the circle is :", area)



























def main(): # Tym zajmuje sie na poczatku

    shape_type = input("Get area of what shape : ")

    get_area(shape_type)



main()
