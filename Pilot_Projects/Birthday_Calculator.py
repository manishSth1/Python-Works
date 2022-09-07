from datetime import date
print("To find out your Birth year")
age = int(input("Enter your age: "))
today = date.today()
result = today.year - age
print(f"Your Birthday Year was: {result}")

print('\n')

print("To find out your age")
birthday = int(input("Enter your Birth year: "))
today = date.today()
age = today.year - birthday
print(f"You are {age} years old.")
