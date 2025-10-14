class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def display_details(self):
        print("Title:", self.title)
        print("Author:", self.author)

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
    def circumference(self):
        return 2 * 3.14 * self.radius

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def increase_salary(self, percent):
        self.salary += self.salary * percent / 100

class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        return a / b

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def check_pass_fail(self):
        if self.marks >= 50:
            print("Pass")
        else:
            print("Fail")

b = Book("Python Basics", "Deitel")
b.display_details()

c = Circle(5)
print("Area:", c.area())
print("Circumference:", c.circumference())

e = Employee("Ali", 50000)
e.increase_salary(10)
print("Updated Salary:", e.salary)

calc = Calculator()
print("Add:", calc.add(5, 3))
print("Subtract:", calc.subtract(5, 3))
print("Multiply:", calc.multiply(5, 3))
print("Divide:", calc.divide(5, 3))

s = Student("Aijaz", 45)
s.check_pass_fail()
