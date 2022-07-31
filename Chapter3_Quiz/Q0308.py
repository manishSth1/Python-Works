my_dictionary = {                            # created a dictionary of a person
    'name': 'Ronald Batman',
    'age': 35,
    'profession': 'Senior Developer',
    'married': False,
} 

#1
print(my_dictionary['name'])                 # accessing value of 'name' from the dictionary

#2
print(f"{my_dictionary['name']} will be {my_dictionary['age'] + 10} years old after 10 years.")   # use of formatted string to add the age by 10 more years

#3
#print(my_dictionary['employed'])           # 'KeyError' will occur

#4
print(my_dictionary.get('employed'))        # will return None because value dosen't exits

#5
print(my_dictionary.get('employed', False))     # prints 'False', we use this when we are not sure if the value exists