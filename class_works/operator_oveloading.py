# operator overloading

class Length:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{self.value} {self.unit}"

    def __add__(self, Length):
        return Length(self.value + other.value, self.unit) # result = Length(l1.value + l2.value, l1.unit)    

    def __gt__(self, other):
        return self.value > other.value
    
l1 = Length(20, 'cm')
l2 = Length(100, 'cm')
print(l1)
print(l1+l2)

if l1> l2:
    print("l1 is greater")
else:
    print("l2 is greater")