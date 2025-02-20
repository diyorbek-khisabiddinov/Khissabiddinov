import math

def area_of_trapezoid(height, first, second):
    return ((first + second) * height)/ 2

height = int(input("Enter the height of trapezoid: "))
first = int(input("Enter the first value: "))
second = int(input("Enter the second value: "))

print(f"Expected output: {area_of_trapezoid(height, first, second)}")