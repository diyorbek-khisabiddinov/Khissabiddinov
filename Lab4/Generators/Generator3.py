def divisible_by3_and4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter the number: "))

for num in divisible_by3_and4(n):
    print(num, end=" ")
    