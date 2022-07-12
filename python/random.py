x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulo")

op = int(input("Enter the chosen operation: "))

if (op == 1):{
    print(x ,"plus", y ,"is equal to", x + y)
}
elif (op == 2):{
    print(x ,"minus", y ,"is equal to", x - y)
}
elif (op == 3):{
    print(x ,"multiplied by", y ,"is equal to", x*y)
}
elif (op == 4):{
    print(x ,"divided by", y ,"is equal to", x/y)
}
elif (op == 5):{
    print(x ,"modulo", y ,"is equal to", x%y)
}
else:{
    print("Invalid Input!!")
}