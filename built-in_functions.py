class Student:
    # class variables / attributes

    def __init__(self, name, id):           # def __init__( function variables/ instance variables)
        self.name = name        # function variable is converted into class variable
        self.id = id            # function variable is converted into class variable

try:
    obj2 = Student("BBB", 101)
    # deletes the attribute age
    delattr(obj2, 'id')
    print(obj2.id)
except:
    print("\n Object's attribute has been deleted ")