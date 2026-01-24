#################################################
# CS03B - Winter 2026
# Assignment 1 - Question 1
# Student Name: Cen Li
# SID: 20713344
#################################################

import math

class Circle:
    def __init__(self,x=0, y=0, radius=1):
        self.x = x
        self.y = y
        self.radius = radius

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        self.radius = radius

    def getArea(self):
        return math.pi * (self.radius ** 2)

    def getPerimeter(self):
        return 2 * math.pi * self.radius

    def distance(self, x, y):
        return math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)

    def containsPoint(self, x, y):
        return self.distance(x, y) <= self.radius

    def containsCircle(self, circle):
        dist = self.distance(circle.get_x(), circle.get_y())
        return dist + circle.get_radius() <= self.radius

    def overlaps(self, circle):
        dist = self.distance(circle.get_x(), circle.get_y())
        return dist <= (self.radius + circle.get_radius())

def run():
    """
    Students should implement their code for Question 1 inside this function.
    """
    c1 = Circle(2, 2, 5.5)
    c2 = Circle(3, 3, 2.0)
    c3 = Circle(10, 10, 1.0)
    c4 = Circle(6, 6, 3.0)

    circles = [c1, c2, c3, c4]

    print("--- Circle Details ---")
    for i, c in enumerate(circles):
        print(f"Circle {i + 1}: Radius={c.get_radius()}, Area={c.getArea():.2f}, Perimeter={c.getPerimeter():.2f}")

        if c.containsPoint(5, 5):
            print(f"  -> Contains point (5, 5)")

    print("\n--- Relationship Checks ---")
    if c1.containsCircle(c2):
        print("Circle 1 contains Circle 2")

    if c1.overlaps(c4):
        print("Circle 1 overlaps with Circle 4")

    print("Hello from Question 1!")



if __name__ == "__main__":
    # This allows students to run this specific file 
    # individually for testing (e.g., `python q1.py`)
    run()