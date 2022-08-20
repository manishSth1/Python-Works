# write a program to find out the factorial of a number
# 0! = 1
# 3 ! = 3 * 2 * 1               =   3 * 2!
# 4 ! = 4 * 3 * 2 * 1           =   4 * 3!
# 5! = 5 * 4 * 3 * 2 * 1        =   5 * 4 !

# x! = x * (x-1) * (x-2) *...*1 =   x * (x-1)!

x = 5


def fact(x):
    result = x
    if x > 0:
        while x > 1:
            x -= 1
            result *= x
    else:
        result = 1
    return result


# Using recursive function
def factorial(x):
    if x <= 0:
        return 1
    # x! = x * (x-1) * (x-2) *...*1 =   x * (x-1)!
    return x * factorial(x - 1)


print(factorial(6))
"""
Explanation

factorial(6)

= 6 * factorial(5)
= 6 * 5 * factorial(4)
= 6 * 5 * 4 * factorial(3)
= 6 * 5 * 4 * 3 * factorial(2)
= 6 * 5 * 4 * 3 * 2 * factorial(1)
= 6 * 5 * 4 * 3 * 2 * 1 * factorial(0)
= 6 * 5 * 4 * 3 * 2 * 1 * 1
= 720
"""

# A recursive function that prints out the first nth itm of a fibonacci series

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# 4, 5, 9, 14, 23, 37, 60
"""
fib(7th)
= 6th + 5th
= [5th + 4th] + [4th + 3rd]
= 4th + 3rd + 3rd + 2nd +3rd + 2nd + 2nd + 1st
= 3rd + 2nd + 2nd + 1st + 2nd + 1st + 2nd + 2nd + 1st + 2nd + 2nd + 1st
= 2nd + 1st + 2nd + 2nd + 1st + 2nd + 1st + 2nd + 2nd + 1st + 2nd + 2nd + 1st
= 5 + 4 + 5 + 5 + 4 + 5 + 4 + 5 + 5 + 4 + 5 + 5 + 4
= 60
"""

first = 4
second = 5


def fib(n):
    if n == 1:
        return first
    elif n == 2:
        return second
    return fib(n - 1) + fib(n - 2)


print(fib(7))

# write a recursive function that prints out the sum of a number in the pattern below
"""
5 = 5 + 4 + 3 + 2 + 1
10 = 10 + 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1
"""

import enum
import sys

sys.setrecursionlimit(10000)


def add_me(n):
    if n <= 1:
        return n
    return n + add_me(n - 1)


print(add_me(5))

# A recursive function to convert decimal to binary
"""
0 = 0
1 = 1
2 = 10
3 = 11
4 = 100
101
110
111
1000
1001
1010
1011
1100
1101
1110
1111

"""

a = 1
b = 2
c = 3

list1 = [1, 2, 3]

output = (list1[0] * 100 + list1[1] * 10 + list1[2])  # 123

print(output)

list2 = [1, 4, 6, 8, 9, 5, 2, 8, 7]


out = 0
for i , v in enumerate(list2[::-1]):
    out += v * (10**i)

print(out)


"""
12345
54321

"""

x = 12345

out1 = 0                     # 54321

while x>0:
    last = x%10             # 1
    out1 = out1*10 + last     # 5432 * 10 + 1
    x = x//10               # 1

print(out1)


def dec2bin(n: int):
    if n != 0:
        return dec2bin(n // 2) * 10 + n % 2
    else:
        return 0


print(dec2bin(1200))  # 110010