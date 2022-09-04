import sys                  # importing sys module

def pound_to_kg(pound):        
    return pound / 2.2

def kg_to_pound(kg):
    return kg * 2.2

if __name__ == '__main__':
    print(sys.argv)
    try:
        option = sys.argv[1]
        value = float(sys.argv[2])
    
    except IndexError:
        print("We need exaxtly 2 arguments to run this program")
        
    except ValueError:
        print("You supplied non-numeric value to convert")
        
    else:
        if option == 'pound_to_kg':
            print(f"{value} pounds equals to {pound_to_kg(value)} kg.")
        if option == 'kg_to_pound':
            print(f"{value} kg equals to {kg_to_pound(value)} pounds.")
            
        
    