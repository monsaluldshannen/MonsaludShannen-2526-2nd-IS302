import math

class Shape:
    def area(self):
        pass  # Base method to override

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius ** 2, 1)

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Example Usage
shapes = [
    Rectangle(10, 5),
    Circle(5),
    Triangle(6, 8)
]

print(f"Rectangle Area: {shapes[0].area()}")
print(f"Circle Area: {shapes[1].area()}")
print(f"Triangle Area: {shapes[2].area()}")