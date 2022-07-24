empty_list = []

#1
empty_list.append(5)
empty_list.append(9)
print(f"The list is {empty_list}.")

#2
x = int(input("Enter a number you want to add in the list: "))
empty_list.append(x)
print(f"The list after you appended {x} is {empty_list}.")

#3
more_items = [1,2,3]
empty_list.extend(more_items)
print(f"The list after extending with {more_items} is {empty_list}.")

#4
print(f"The length of the list is {len(empty_list)}.")

#5
print(f"The list before popping out second item is {empty_list}.")
empty_list.pop(1)
print(f"The list after popping out second item is {empty_list}.")
