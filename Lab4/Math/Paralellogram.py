import math

def area_of_parallelogram(length, height):
    return length * height

length = float(input("Enter the length of base: "))
height = float(input("Enter the height of parallelogram: "))

print(f"Expected output: {area_of_parallelogram(length, height)}")