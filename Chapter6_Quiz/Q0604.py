
def mul_table(number, limit=10):
    print(f'[Table of {number} ]'.center(34, '-'))
    print(f'|{"number".center(10)}|{"mul".center(10)}|{"result".center(10)}|')
    mul = 1
    for i in range(1, limit+1):
        print(f'|{number:>9} |{mul:>9} |{(number * mul):>9} |')
        mul += 1

number = int(input("Enter a number you want multiplication table for: "))
limit = int(input("Enter the number to which multiplies are printed: "))

mul_table(number, limit)


