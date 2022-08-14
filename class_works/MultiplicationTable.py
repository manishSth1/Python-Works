num = 1
while num <= 10:
    mul = 1
    print(f'[Table of {num} ]'.center(34, '-'))
    print(f'|{"number".center(10)}|{"mul".center(10)}|{"result".center(10)}|')
    print('-'*34)
    while mul <= 10:
        print(f'|{num:>8} |{mul:>8} |{(num * mul):>8} |')
        mul += 1
    print("-"* 34)
    print()
    num += 1