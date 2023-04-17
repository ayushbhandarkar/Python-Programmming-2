class Area:
    def __init__(self, length, width):
        self.length = length
        self.width = width


class Square(Area):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area_sqr(self):
        return self.length * self.width


class Cube(Area):
    def __init__(self, length, width, height):
        self.height = height
        super(Cube, self).__init__(length, width)

    def area_Cube(self):
        return self.width * self.length * self.height


obj_sqr = Square(3, 4)
print("Area of square : ", obj_sqr.area_sqr())
