class Person:                # creating a class named "Person"
    weight = float           # class attribute
    def __init__(self, name, age, gender): # instance attributes
        self.name = name           
        self.age = age
        self.gender = gender
    def year_of_birth(self):     # returns the year by subtracting the age from the current year
        return 2022 - self.age
    def get_pronouns(self):      # returns list of ['he', 'his', 'him'] or ['she', 'her', 'hers'] by checking the gender
        if self.gender == 'M':
            print(['he', 'his', 'him'])
        elif self.gender == 'F':
            print(['she', 'her', 'hers'])
        else:
            print("Invalid input")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ")
person1 = Person(name, age, gender)
print('\n')
print(f"Name is: {person1.name}")
print(f"Age is: {person1.age}")
print(f"Your pronouns are: ", end = '')
person1.get_pronouns()
print(f"Your date of birth is: {person1.year_of_birth()}")   