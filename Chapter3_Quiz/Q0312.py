#1

PI = 3.1415
print(int(PI))  # the int() function can add a floating-point number inside of the parentheses to convert it to an integer, here Python cuts off the decimal and remaining numbers of a float to create an integer

#2

str_1 = "20"
str_2 = "30"
print(str_1 + str_2)     # gives "2030"
str_1 = int(str_1)       # use int() to convert into int
str_2 = int(str_2)       # use int() to convert into int
print(str_1 + str_2)     # gives "50"

#3

x = ['1','2', '3', '4', '5']
res_sum = 0
res_sum = sum(int(i) for i in x)
print(res_sum)

#4

odd = [1, 3, 5, 7, 9, 11, 13, 15]
prime = [2, 3, 5, 7, 11, 13, 17]

odd_not_prime = []
either_odd_or_prime = []
prime_not_odd = []

for num in odd:
    if num not in prime:
        odd_not_prime.append(num)

for num in odd:
    if num in prime:
        either_odd_or_prime.append(num)

for num in prime:
    if num not in odd:
        prime_not_odd.append(num)

print("Numbers that are odd but not prime:", odd_not_prime)
print("Numbers that are either odd or prime:", either_odd_or_prime)
print("Numbers that are prime but not odd:", prime_not_odd)