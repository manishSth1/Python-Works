import json                            # importing json (JavaScript Object Notation) -> data interchange format such as XML, CSV

person = {                             # creating a dictionary named "person"
    "name":"John Doe",
    'age':20,
    'married':False,
    'occupation':'programmer',
    'organization': None,
    'programming_languages': [
        {
            "name": "Python",
            "version": 3.9,
            'level': "Beginner",
        },
        {
            "name": "Java",
            "version": 17,
            'level': "Expert",
        },
        {
            "name": "C++",
            "version": 2019,
            'level': "Mid",
        },
    ]
}


# print(json.dumps(person, indent=2))
with open("class_works/person_1.json", 'w') as file:       # open a file named "person_1.json" in 'write' mode
    json.dump(person, file, indent=2)                      # change 'person' dictionary into 'json' into jason file, use 'dump', indent 2 -> standard indentation for json


with open("class_works/person_1.json", 'r') as file:       # open a file named "person_1.json" in 'read' mode
    person2 = json.load(file)                              # use 'load' to laod in a 'file'

print(person2)                                             # prints 'person2' in console


str1 = json.dumps(person)                                  # use 'dumps' unlike used 'dump' for file

#print(str1)                                               # prints in console

str2 = '{"name": "C++", "version": 2019, "level": "Mid"}'  # use 'loads' for str unlike 'load' for file

obj1 = json.loads(str2)                                   

print()                                                    # prints new line

print(obj1)                                                # prints in single line