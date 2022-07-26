rate = 20
apples = int(input("Enter number of apples you want to buy: "))

print(f"Your total payable amount is: ${rate * apples}")

x = 5
x: int = 5.34   # type hinting is wrong, it should be a float. It ignores the data type given - which is optional
print(x)
print(type(x))

x = input("ENTER: ")
if x.isnumeric():
    x = int(x)
else:
    print("Wrong input")

students = ["Abraham", "Jack", "John"]
prof = students
students[0] = "Manish"
print(prof)

students = [2, 3, 5, 6, 7]
students.append(8)   # can append at the end of the list
students.insert(0, 1) # can insert to any given indeces
more_students = [9,10,11]  # create a variable that has more items
students.extend(more_students) # extend can add all items provided in the variable
print(students)

even = [2,4,6,8,10,12,14,16]
even.pop() # removes last item
print(even)

even = [2,4,6,8,10,12,14]
value = even.pop()
print(f"The popped out value is: {value}")

xyz = []
xyz.pop() # popping out empty list throws out error

even = [2,4,6,8,10,12,14]
value = even.pop(-6)    # give index 1
print(f"The popped out value is: {value}")
print(even)

fib = [0,1,1,2,3,5,8,13,21]
fib.remove(13)   # removes an element from a list 
print(fib)       # if we remove 1, it will just remove one 1, the first one
print(len(fib))
print(fib.__len__())    # dunder, efficient than len(), cause len() will call __len__()

fib = [0,1,1,2,3,5,8,13,21]
fib.clear()      # clear() clears the whole list
# if del fib[] will delete, won't return empty list
print(fib)

# memory deallocate, garbage collection
# use del() function to delete memory location, cause variables would be taking space to full memory
x = 5
print(x)
del x         # 
print(x)

fib = [0,1,1,2,3,5,8,13,21]
del fib[0:3], fib[5]  # del can remove slice and also individual elements
print(fib)

fib = [0,1,1,2,3,5,8,13,21]
fib *= 0   # works as clear function
print(fib)

fib = [0,1,1,2,3,5,8,13,21]
del fib   # not clears, but delete the list
print(fib)   # fib list won't be defined as it is deleted

a = 5
b = a   # just assigning value of a is same for b, but not a = b, value passed but not reference
b += 2
print(a)
print(b)

x = [1,2,3,5,8]
y = x
y.pop()
print(x)    # same result, passed by reference, sets each other values equal
print(y)

x = [1,2,3,5,8]
y = x.copy()   # keeps original but when changes, allocate in new memory, passed by reference or address, increases memory usage, if viewed in task manager
y.pop()
print(x)    
print(y)

x = [1,"Manish", 2, 3, "Samuel", 5, 8]
x.reverse()    # reverses the list
print(x)

# reverse using slice
x = [1,"Manish", 2, 3, "Samuel", 5, 8]
x = x[::-1]  #comes back from and no index given
print(x)

x = [1,2,3,5,8]
print(x[1:3:1])  # get element and skip one element

x = [25,2,5,98,66,100,25,4,0,1]
x.sort()  # sorts in ascending order
print(x)

x = [25,2,5,98,66,100,25,4,0,1]
x.sort(reverse=True)  # sorts in descending order
print(x)

x = [25,2,5,98,66,100,25,4,0,1]
x = sorted(x)  # returns value, double use of memory like .copy()
print(x)

x = [25,2,5,98,66,100,25,4,0,1]
x = sorted(x, reverse=True)  # returns value, double use of memory like .copy()
print(x)

x = [25,2,5,98,66,100,25,4,0,1]
x.sort() 
print(x)
print(x.index(66))    # to find out index = list.index(list)element)

# counting the number of items
x = [25,2,5,98,66,100,25,4,0,1,25,98,4,5,3,25]
print(x.count(25))  # to count items in list = list.count(list_element)

# Tuples
# tuples are immutble sequence (values cannot be changed like that in list)
# represented with comma separated values enclosed by parentheses
# tuples are faster than list

tup_1 = () # empty tuple
print(type(x))

tup_2 = (1,2,3,4)   # same data type
print(tup_2)

tup_3 = (1, 2, "John", 4.5, True)   # different data type
print(tup_3)
tup_3    # in Jupyter Notebook, no need to use print function, can work

list_1 = [1, 2, 4, 5,]     # can use comma at end of list and tuples as well
tup_4 = tuple(list_1) 
print(tup_4)

tup = ('john')    # generally we put statement in (). Example - (5+4) * (7-5) = 9 * 2 = 18. They are not tuples, only grouped
print(tup)
type(tup)     # gives string

tup_5 = (
        'John'
        'Doe'
        )        # if used in () and not puta comma for, then it's not a tuple
print(type(tup_5))


# so put cooma to make a tuple
tup = ('John',)
print(tup)
print(type(tup))

t1: tuple = (1, 2, 3)   # type hinting, way to declare data types
print(type(t1))

y: bool = True
print(type(y))

tup_3 = (1, 2, "John", 4.5, True)
print(tup_3[0])
print(tup_3[-1])

x = [-2,47,53,1,2,3,7,8]
print(x[1:9:1])
print(x[1:9:2])
print(x[0:9:2])
print(x[::2])
print(x[1:9:3])
print(x[-4:-1])

odd = (1, 3, 6)     # can't use .appen() as in list
odd_new = (7,)
odd1 = odd + odd_new
print(odd1)

odd = (1,3,5,7,9,11,13,15)
odd = list(odd)   # re-declare to list
odd[-1] = 17    
print(odd)
odd = tuple(odd) # convert to tuple from list

odd = (1,3,5,7,9,11,13,15)
odd = tuple(list(odd[0:7]))
print(odd)

odd = (1,3,5,7,9,11,13,15)
odd = tuple(list(odd[:-1]) + [17])
print(odd)

odd = (1,3,5,7,9,11,13,15)
odd = odd[:-1] + (17,)
print(odd)

t1 = (1, 2, 3)
t1 = t1 + (4, 5, 6)   # adding tuples
print(t1)

# unpacking
x = [1, 2, 3]
y = [4, 5, 6]
z = x + y
print([x, y])   # two list in list
print(*x, *y)   # removes []of x when *x, removes again []of y when *y
print(*x, y)     # removes []of x when *x but prints []of y
print([*x, *y])  # prints inside a list
print([x + y])  # list in list
print(z)        # single list

#unpacking
odd = (1,3,5,7,9,11,13,15)
odd = (*odd[:-1], 17)   # removes last element(15) and place 17
print(odd)

x = (1,2,3,7,8,9)
print(len(x))
x = (*x[:3], 4,5,6, *x[3:])  # puts value in where we need to using unpacking
print(x)

x = (1,2,3,7,8,9,1,1,5)
print(x.count(1))
print(x.index(2))
