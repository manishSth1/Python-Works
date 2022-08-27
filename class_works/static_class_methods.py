class Length:
    cm_inch_mul_factor = 2.54

    @classmethod
    def get_multiplication_factor(cls):
        return cls.cm_inch_mul_factor

    @staticmethod
    def cm_to_inches(cm):
        return cm / 2.54

    @staticmethod
    def inch_to_cm(inch):
        return inch * 2.54

    def __init__(self, cm) -> None:
        self.cm = cm

    def inches(self):
        return self.cm / self.get_multiplication_factor()

l1 = Length(30)
print(l1.inches())
l1.cm_inch_mul_factor = 5.54
print(l1.inches())