n = int(input("Enter the number: "))
def count(n):
    while n >= 0:
        yield n
        n = n - 1
for i in count(n):
    print(i)