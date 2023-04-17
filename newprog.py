class Employee:
    count = 0

    def __init__(self):
        self.count = self.count + 1

    def display(self):
        print("The number of employees", self.count)


emp = Employee()
emp2 = Employee()

emp.display()
emp2.display()