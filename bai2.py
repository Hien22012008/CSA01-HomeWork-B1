import math


class Rectangle:
    def __init__(self, height: float, width: float):
        self.height = height
        self.width = width

    def perimeter(self):
        return 2 * (self.height + self.width)

    def area(self):
        return self.height * self.width


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius**2


shape = input("Shape (rectangle/circle): ")

if shape == "rectangle":
    height = float(input("Height: "))
    width = float(input("Width: "))
    rectangle = Rectangle(height, width)
    print(f"\n=> Perimeter: {rectangle.perimeter()}")
    print(f"=> Area: {rectangle.area()}")
elif shape == "circle":
    radius = float(input("Radius: "))
    circle = Circle(radius)
    print(f"\n=> Perimeter: {circle.perimeter()}")
    print(f"=> Area: {circle.area()}")
else:
    print("\n=> Invalid!")
