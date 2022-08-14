# Pattern 1
"""
*
*   *
*   *   *
*   *   *   *
*   *   *   *   *
"""
for i in range(1,6):
    for j in range(1,i+1):
        print("*", end = "   ")
    print()
print('\n')

# Pattern 2
"""
1
1   3
1   3   5
1   3   5   7
1   3   5   7   9
"""
for i in range(5):
    for j in range(1, i+2):
        j = j*2-1
        print(j, end = "   ")
    print()
print('\n')

# Pattern 3
"""
1
2   2
3   3   3
4   4   4   4
5   5   5   5   5
"""
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end="   ")
    print()
print('\n')

# Pattern 4
"""
1
2   1
3   2   1
4   3   2   1
5   4   3   2   1
"""
for i in range(1,6):
    for j in range(i,0,-1):
        print(j, end= "   ")
    print()
print('\n')

# Pattern 5
"""
1   2   3   4   5
2   4   6   8   10
3   6   9   12  15
4   8   12  16  20
5   10  15  20  25
"""
for i in range(1,6):
    for j in range(1,6):
        print(i*j,end="   ")
    print()
print('\n')

# Pattern 6
"""
A
A   P
A   P   P
A   P   P   L
A   P   P   L   E
"""
word = "APPLE"
length = len(word)
for i in range(length):
    for j in range(i+1):
        print(word[j], end="   ")
    print()
print('\n')

# Pattern 7

for i in range(1,6):
    for j in range(5-i):
        print(" ", end=" ")
    for j in range(1,i+1):
        print("*", end = " ")
    print()
print('\n')

# Pattern 8
for i in range(1,6):
    for j in range(5-i):
        print(" ", end=" ")
    for j in range(1,i+1):
        j = j*2-1
        print(j, end = " ")
    print()
print('\n')

# Pattern 9
word = "APPLE"
length = len(word)
for i in range(length):
    for j in range(length-i):
        print(" ", end=" ")
    for j in range(0,i+1):
        print(word[j], end = " ")
    print()
print('\n')

# Pattern 10
for i in range(1,6):
    for j in range(5-i):
        print(" ", end=" ")
    for j in range(1,i):
        print(j, end = " ")
    for j in range(i,0,-1):
        print(j, end = " ")  
    print()
