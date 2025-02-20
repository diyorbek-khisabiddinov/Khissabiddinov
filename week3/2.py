class calculator():
    def div(self, a, b):
        if b==0:
            return "Number can not be divisible to 0"
        return a/b
    def mult(self, a, b):
        return a*b
    def add(self, a,b):
        return a+b
    def subt(self, a, b):
        return a-b
calc = calculator()
str = input("Choose operator:")
a = int(input("Enter the first operand:"))
b = int(input("Enter the second operand:"))
if str == "ad":
    print(calc.add(a,b))
elif str == "div":
    print(calc.add(2,3))