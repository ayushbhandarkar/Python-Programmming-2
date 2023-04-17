class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

obj = Car("ford", "figo", 2020, "red")
print(obj.color)
print(obj.year)
print(obj.model)
print(obj.make)

obj2 = Car("maruti", "ertiga", 2021, "white")