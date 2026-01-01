class Shape:
    def area(self):
        raise NotImplementedError("derived classes need to override this method")
class Rectangle(Shape):
    def __init__ (self, width, length):
        self.width = width
        self.length = length
    def area(self):
        return self.width * self.length
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)
from polymorphism_demo import Shape, Rectangle, Circle
import math

def main():
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()