def square_(n):
    for i in range(n+1):
        yield i ** 2
n=int(input("put the number:"))
for square in square_(n):
    print(square,end=" ")

    