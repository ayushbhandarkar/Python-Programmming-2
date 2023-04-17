class Employee:
    emp_name = ""
    emp_id = 0

    def func(self, _name, id):               # parameterized constructor
        self.emp_id = id
        self.emp_name = _name
        print(" Employee name : ", self.emp_name)
        print(" Employee id : ", self.emp_id)


emp = Employee()
emp.func("Disha", 101)
