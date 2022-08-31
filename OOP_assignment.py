class School:
    
    def __init__(self, name, classrooms, teachers, students):
        self.name = name
        self.classrooms = classrooms
        self.teachers = teachers
        self.students = students

s1 = School("Baruch College", 35, 40, 1000)
print(s1.name)
        
class Classroom:
    
    def __init__(self, number, board, desks, windows, chairs):
        self.number = number
        self.board = board
        self.desks = desks
        self.windows = windows
        self.chairs = chairs

c1 = Classroom(405, ["6x6", "White"], 25, 4, 55 )   
print(c1.board)  

class Board:
    
    def __init__(self, dimension, color):
        self.dimension = dimension
        self.color = color
        
class Teacher:
    
    def __init__(self, name, subject, time):
        self.name = name
        self.subject = subject
        self.time = time
    
    def subjects(self):
        names = {
            1: "CIS 2200",
            2: "CIS 2300",
            3: "CIS 3100",
            4: "CIS 3400",
            5: "CIS 3920",
            6: "CIS 5800"
        }
        
    
    def __init__(self, complexity, scope):
        self.complexity = complexity
        self.scope = scope

class Student:
    
    def __init__(self, roll, name, majors):
        self.roll = roll
        self.name = name
        self.majors = majors


    
 