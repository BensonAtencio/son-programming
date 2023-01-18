class Person:
    numberOfPerson = 0
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        Person.numberOfPerson += 1

    def greet(self):
        print(f"Hi my name is {self.name}, {self.height}cm and I am {self.age} years old")

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Height: {self.height}cm"

    def __del__(self):
        Person.amount -=1

    def getOlder(self):
        self.age += years

# inheritance po itong part nato
class Worker(Person):
    def __init__(self, name, age, height, salary):
        super(Worker, self).__init__(name, age, height)
        self.salary = salary

    def calcSal(self):
        return self.salary*12

    def __str__(self):
        text = super(Worker, self).__str__()
        text += f", Salary: {self.salary}"
        return text

worker1 = Worker("Hannah Kaye", 21, 166, 100000)
print(worker1)
print(worker1.calcSal())

# person1 = Person("Mike Enriquez", 22, 166)
# person2 = Person("Mikel Henriquez", 22, 172)
# # del person1
# # print(person1.fName)
# # print(person1.lName)
# # print(person1.greet())
# print(person1)
# # print(Person.amount)

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"X: {self.x}, Y: {self.y}"

v1 = Vector(2, 5)
v2 = Vector(6, 3)

print(v1)
print(v2)

v3 = v1 + v2

print(v3)