# Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Child class - Inheritance
class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def display_student(self):
        self.display_person()
        print("Course:", self.course)


# Object
student1 = Student("Muhsin", 23, "Python Full Stack")

student1.display_student()


# Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


account = BankAccount(5000)

account.deposit(2000)

print("\nBank Account Balance:", account.get_balance())