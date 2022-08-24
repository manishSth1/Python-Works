# 5 different classes
class Person:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
p1 = Person("John", 36, 175)
print(p1.name)
print(p1.weight)

class Car:
    def __init__(self, make, model, year, color, price):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.price = price
c1 = Car("Mercedes", "GLC 300", 2022, "Matic", 75000)
print(c1.make)
print(c1.price)

class Chair:
    def __init__(self, material, color, price):
        self.material = material
        self.color = color
        self.price = price
c2 = Chair("Wooden", "Brown", 150)
print(c2.material)

class Laptop:
    def __init__(self, make, model, price):
        self.make = make
        self.model = model
        self.price = price
l1 = Laptop("Dell", "Inspiron 15 3000", 1100)
print(l1.model)

class Phone:
    def __init__(self, make, model, color, price):
        self.make = make
        self.model = model
        self.color = color
        self.price = price
p1 = Phone("Apple", "XR", "White", 750)
print(p1.model)
print(p1.price)