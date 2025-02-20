class calculator():
    def multiplication():
        a = int(input("Enter the first operand:"))
        b = int(input("Enter the second operand:"))
        return a*b
    def division():
        a = int(input("Enter the first operand:"))
        b = int(input("Enter the second operand:"))
        return a/b

str = input("Choose operator:")
if str == "m":
    print(multiplication())