# using %s, %d, %f

first_name = "Manish"
last_name = "Shrestha"

age = 24

height = 5.9 

full_name = "My name is" + ' ' + first_name + ' ' + last_name + "." + \
    " I am " + str(age) + " years old." + ' ' + "My height is " + str(height) + "."

print(full_name)

full_name2 = "My name is %s %s." " I am %d years old." " My height is %f." %(first_name, last_name, age, height) 
print(full_name2)

# padding %[a]b %[a]%[b]

data = "      May Name.   "
print(data.strip(), "Next Value")    # remove spaces and add

text = "Hello, I am John"

print(text[0])   # first position value H

print(text[7])   # 7th position value I

print(text[15])   # 15th position value n

# also with negative index

print(text[-1])   # prints n, from reverse position

print(text[-7])  # prints a of am

# positive index - starts from 0 and negative index starts from -1

# extracting more than 1 characters

print(text[0:5])   # inclusive 0, exclusive 5

print(text[12:16])

print(text[9:11]) 

print(text[7:]) # if no end interval specified will give till end

print(text[:8]) # if no open index in front specified, will print whatever is in front

print(text[-11:-5])    # I am

print(text[-4:])      # John

print(text[-16:-11])  # Hello

print(text[-9:11])    # I am

print(text[7:-5])    # I am

# Extracting substrings with step

print(text[0:5:2])    # Hlo, leave 2 characters

print(text[0:5:1])    # Hello

print(text[4::-1])   # prints in reverse order

print(text[::-1])   # reverses whole string



