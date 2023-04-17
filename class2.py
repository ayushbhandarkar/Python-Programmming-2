class Sample:
    num1 = 0
    num2 = 0

    def display(ref, value1, value2):
        ref.num1 = value1
        ref.num2 = value2
        print(" Num : ", ref.num1)
        print(" Num : ", ref.num2)


obj = Sample()
del obj             # object has been deleted
obj.display(20, 30)
