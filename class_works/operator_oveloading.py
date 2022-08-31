# operator overloading

class Length:                # create a class Length that takes two attributes value and unit
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def __str__(self):                    # returns "value unit" -> 20 cm
        return f"{self.value} {self.unit}"
        
    def __add__(self, other: "Length"):
        return Length(self.value + other.value, self.unit) # result = Length(l1.value + l2.value, unit)    

    def __gt__(self, other):
        return self.value > other.value
    
l1 = Length(20, 'cm')
l2 = Length(100, 'cm')
print(l1)
print(l1+l2)
l3 = l1 + l2
print(l3)

if l1> l2:
    print("l1 is greater")
else:
    print("l2 is greater")