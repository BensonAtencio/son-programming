# Simple Calculator Python with the use of classes

class Calculator():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, x,y):
        print(x,"+",y, "=", x+y)

    def sub(self, x,y):
        print(x,"-",y, "=", x-y)

    def mult(self, x, y):
        print(x,"*",y, "=", x*y)

    def div(self, x, y):
        if(y == 0):
            print("Cannot divide by zero")

        else:
            print(x,"/",y, "=", x/y)

a = int(input("PLease enter first number: "))
b = int(input("Please enter second number: "))
calc = Calculator(a,b)

print("Choose operation")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")
c = int(input("Choice: "))

if(c == 1):
    calc.add(a, b)
elif(c == 2):
    calc.sub(a, b)
elif(c == 3):
    calc.mult(a, b)
elif(c == 4):
    calc.div(a,b)
else:
    print("Wrong Choice")
