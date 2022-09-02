def divide(a, b):
    try:
        print(f"I'm trying to solve the problem: {a} / {b}")
        x = a / b
        print("Hey I solved it: ", end = "" )
        print(x)

    except ZeroDivisionError:                                      # for error with division with zero  
        print("Hey, Here comes an error : Zero Division Error")

    except TypeError as e:                                         # for TypeError -> such as string divided with int
        print(f"Error Spotted: {e}")

    except Exception as e:                                         # general error need to write at the end, "known errors" write above it
        print(f"An Unknown Error occured. The error is: {e}")

divide("abc", 10)    # TypeError is handled
divide(10, "a")      # TypeError is handled
divide(1, 0)         # ZeroDivisionError is handled
divide(2,2)          # no error, it solves, give the result
