first_name = "Manish"
last_name = "Shrestha"

# 1 with concatentation
full_name = "My name is " + first_name + " " + last_name
print(full_name)

# 2 with format
print("My name is {} {}".format(first_name, last_name))

# 3 with f string
print(f"My name is {first_name} {last_name}")

# 4 
print("My name is %s %s" %(first_name, last_name))