# Default constructor

class Student:
    roll_num = 101
    __name = "Joseph"

    def display(self):
        print(self.roll_num, self._name)


st = Student()
st.__name = "John"

st.display()
