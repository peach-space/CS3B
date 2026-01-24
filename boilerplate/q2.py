#################################################
# CS03B - Winter 2026
# Assignment 1 - Question 2
# Student Name: Cen Li
# SID: 20713344
#################################################

import math

class Triangle:
    def __init__(self, side1=1.0, side2=1.0, side3=1.0):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_side1(self):
        return self.side1

    def get_side2(self):
        return self.side2

    def get_side3(self):
        return self.side3

    def getPerimeter(self):
        return self.side1 + self.side2 + self.side3

    def getArea(self):
        p = self.getPerimeter() / 2
        area = math.sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3))
        return area

    def toString(self):
        return f"Triangle: side1={self.side1}, side2={self.side2}, side3={self.side3}"

def run():
    """
    Students should implement their code for Question 2 inside this function.
    """
    print("--- Triangle 1 (Default) ---")
    t1 = Triangle()
    print(t1.toString())
    print(f"Area: {t1.getArea():.2f}")
    print(f"Perimeter: {t1.getPerimeter():.2f}")

    print("\n--- Triangle 2 (User Defined) ---")
    t2 = Triangle(3, 4, 5)
    print(t2.toString())
    print(f"Area: {t2.getArea():.2f}")
    print(f"Perimeter: {t2.getPerimeter():.2f}")

    print("Hello from Question 2! ")


if __name__ == "__main__":
    # This allows students to run this specific file 
    # individually for testing (e.g., `python q1.py`)
    run()