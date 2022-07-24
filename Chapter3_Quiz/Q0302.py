wild = ['tiger', 'lion', 'deer', 'bear', 'zebra']  # creating list with animal names

#1
wild.sort()
print(f"The list after sorting in ascending order is {wild}")   # sorting out list in the ascending order

#2
wild.reverse()
print(f"The list after reversing is {wild}")     # reversing the list with .reverse() function

#3
wild.extend(['leopard', 'elephant', 'rhino'])
print(f"The list after extending more animals is {wild}")   # extending more animals to the list

#4
print(f"The index of leopard is {wild.index('leopard')}")     # getting the index of 'leopard' in the list with .index() func

index = wild.index('leopard')
wild.pop(index)                                     # removing the index where the 'leopard' is
print(f"The list after removing leopard is {wild}")

# index = wild.index('leopard')     # error occured because 'leopard' has already been removed from the list

#5
wild.insert(2, 'leopard')                    # inserting 'leopard' into the list at 2 index
print(f"The list after re-adding leopard is {wild}")

#6
wild.remove('rhino')                       # removing 'rhino' from the list
print(f"The list after removing rhino is {wild}")