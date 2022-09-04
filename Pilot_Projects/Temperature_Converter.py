menu ='''                              
    Temperature Converter:
    
    1. Celsius to Fahrenheit
    2. Fahrenheit to Celsius
    '''                             # put menu in a variable

while True:                         # run until it's true
    print(menu)                     # prints out menu set in a variavle
    try:                            # use for exceptional handling -> for ValueError
        option = int(input('Enter the option: '))
        if option == 1:
            c = float(input('Enter the temperature in Celsius: '))
            f = c * 9/5 + 32
            print(f'The value in Fahrenheit is: {f}')
        if option == 2:
            f = float(input('Enter the temperature in Fahrenheit: '))
            c = (f - 32) * 5/9
            print(f'The value in Celsius is: {c}')
        else:
            print(f'No such option {option}')
    except ValueError:
        print('Invalid input!!')
    
    message = input('Do you want to convert again? [y/n]: ')
    if message.lower() != 'y':
        exit()