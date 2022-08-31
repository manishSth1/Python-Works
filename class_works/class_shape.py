class Point:
    x = 0
    y = 0
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return(f"Point ({self.x}, {self.y})")
    
p1 = Point(2,1)
print(p1)
p2 = Point(4,3)
print(p2)

class Shape:
    """
    This is a sample shape class which is capable of adding multiple points
    """
    
    def __init__(self):
        self.__points = []    # initialize set, emptset, so that we can append new points to the set
        self.is_plane = True
        
    def add_points(self, p: Point):
        self.__points.append(p)
        if len(self.__points) > 3:
            self.is_plane = False
        else:
            self.is_plane = True
        
    def type(self):
        types = {
            1: "Point",
            2: "Line",
            3: "Triangle",
            4: "Quadrilateral",
            5: "Pentagon",
            6: "Hexagon"
        }
        return types.get(len(self.__points), "Unknown")
        
    def __str__(self):
        return f"Shape: {self.type()}"
    
shape1 = Shape()
print(shape1)
shape1.add_points(p1)
print(shape1)
shape1.add_points(p2)
print(shape1)
shape1.add_points(Point(5,2))
print(shape1) 
print(shape1.__doc__)    # .__doc__ gives the documentation