
tuple_1 = (1, 'apple', 2, 'banana', 3, 1, 3, 'cat', 'cat', 2, 3.5, 1, 1, 5, 8.6, False, 7.9, 1)  # created a tuple with different data types

#1 
print(tuple_1.__len__())   # finding the length of tuple using dunder function
print(len(tuple_1))        # finding the length of tuple using len() function which at the end calls dunder function

#2
print(tuple_1.count(1))     # counting the number of element:'1' in the tuple using .count() func
print(tuple_1.count('cat')) # counting the number of element:'cat' in the tuple using .count() func

#3
print(tuple_1.index(1))        # finding the index of element:'1' -> which gives 0 because it checks from left to right
print(tuple_1.index(1, 15))    # finding the index of element:'1' beyond index 15
#print(tuple_1.index(6))       # will give error because the given element is not in the tuple
print(tuple_1.index('apple'))  # finding the index of element:'apple' using .index() func
