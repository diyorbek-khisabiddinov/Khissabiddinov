def square_alloff(a, b):
    for i in range(a, b + 1):
        yield i ** 2  


a = int(input("Enter the number A: "))
b = int(input("Enter the number B: "))


for square in square_alloff(a, b):
    print(square, end=" ")