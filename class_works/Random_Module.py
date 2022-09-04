import random                                       # Importing random module
print(random.randint(22,35))                        # Printing out a random number from a range 22 to 35

print('\n')                                         # Printing out a anew line

for _ in range(10):                                
    print(random.randint(1,6))                      # Printing out 10 random numbers from a range 1 to 6

print('\n')

options = "12345ABCDEabcde"
print(random.choice(options))                       # Printing out a random character from a string

print('\n')

options = "12345ABCDEabcde"
print(random.choices(options, k=5))                 # Printing out 5 random characters as a list from a string

print('\n')

options = "12345ABCDEabcde"
print(''.join(random.choices(options, k=8)))        # Printing out a random password string with 8 characters

print('\n')

options = 'adhdj$$&&322bdd2447852ddndjj####@@@!!sd'
password = (''.join(random.choices(options, k=8)))
print(password)

"""
random.seed() -> initializes the random number generator

random.randrange() -> accepts 3 parameters start, stop, and step which is similar to range() function. 
                      It returns the random from the eligible numbers from the range function.

random.randint() -> similar to randrange() method but the stop number is inclusive

random.choice() -> chooses a character from the string provided

random.choices() -> chooses a character from the string provided

join(random.choices()) -> chooses characters from the list of string provided and joins them

"""