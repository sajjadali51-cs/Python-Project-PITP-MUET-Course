class Employee:
    total_employees = 0  # class variable to track total employees

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1  

    def display_details(self):  # instance method
        print(f"Name: {self.name}, Salary: {self.salary}")

    @classmethod
    def total_count(cls):  # class method
        print(f"Total Employees: {cls.total_employees}")


# Testing Employee class
e1 = Employee("Alisha", 50000)
e2 = Employee("Sara khan", 60000)
e1.display_details()
e2.display_details()
Employee.total_count()



class Math:
    @staticmethod
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True


# Testing Math class
print("\nPrime check:")
print("5 is prime:", Math.is_prime(5))
print("8 is prime:", Math.is_prime(8))


class Account:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print("Balance cannot be negative!")
        else:
            self._balance = amount


# Testing Account class
print("\nAccount test:")
acc = Account(1000)
print("Current Balance:", acc.balance)
acc.balance = 2000
print("Updated Balance:", acc.balance)
acc.balance = -500 


class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print(f"'{self.title}' by {self.author}, Price: {self.price}")


# Testing Book class
print("\nBooks:")
b1 = Book("Python Basics", "Amjad", 700)
b2 = Book("AI for Everyone", "Asad ", 850)
b3 = Book("Data Science 101", "Ali Muhammad", 950)

b1.display()
b2.display()
b3.display()
