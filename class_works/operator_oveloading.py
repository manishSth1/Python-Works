# operator overloading

class Length:                                  # create a class Length that takes two attributes value and unit
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def __str__(self):                         # returns "value unit" -> 20 cm
        return f"{self.value} {self.unit}"
        
    def __add__(self, other: "Length"):
        return Length(self.value + other.value, self.unit)      # result = Length(l1.value + l2.value, unit)    

    def __gt__(self, other: "Length"):           # operator overloading greater than -> __gt__(self, other)
        return self.value > other.value

    def __sub__(self, other: "Length"):          # operator overloading subtraction -> __sub__(self, other)
        return Length(self.value - other.value, self.unit)
    
    def __ge__(self, other: "Length"):           # operator overloading greater than or equal to -> __ge__(self, other)
        return self.value >= other.value
    
    def __mul__(self, other: "Length"):          # operator overloading multiplication method -> __mul__(self, other)
        return Length(self.value * other.value, self.unit)
    
    def __truediv__(self, other: "Length"):      # operator overloading division method -> __truediv__(self, other)
        return Length(self.value / other.value, self.unit)
    
l1 = Length(20, 'cm')
l2 = Length(100, 'cm')
print(l2 - l1)          # result -> 80 cm
print(l1)               # result -> 20 cm
print(l1+l2)            # result -> 120 cm
l3 = l1 + l2
print(l3)               # result -> 120 cm
l4 = l1 * l2
print(l4)               # result -> 2000 cm

l5 = l2 / l1
print(l5)               # result -> 5.0 cm

if l1> l2:
    print(f"{l1} is greater than {l2}")
else:
    print(f"{l2} is greater than {l1}")     # prints -> 100 cm is greater than 20 cm

if l1 >= l2:
    print(f" {l1} is greater than or equal to {l2}")
else:
    print(f"{l2} is greater than {l1}")    # prints -> 100 cm is greater than 20 cm