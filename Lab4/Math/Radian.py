import math

def degree_to_radian(degree):
    return degree * (math.pi / 180)

degree = float(input("Enter the angle in degrees: "))
print(f"Output radian: {degree_to_radian(degree)}")