class CustomException(Exception):
    pass

def get_point():
    x = int(input("Enter x : "))
    y = int(input("Enter y : "))
    if x > 20 or y > 20:
        raise CustomException
        print(x, y)
        
try:
    p = get_point()
    print(p)
except CustomException:
    print("Point out of bounds")

class JohnError(BaseException):
    def __str__(self):
        return 'You can not use name John'

try:
    name = input("Enter name: ")
    if name.lower() == 'john':
        raise JohnError
except JohnError:
    print("I can not use name John")