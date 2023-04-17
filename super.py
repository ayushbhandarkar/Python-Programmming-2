# wap to implement super function

class Area:
    def __init__(self, length, width):
        self.length = length
        self.width = width


class Square(Area):
    def __init__(self, length, width):
        super().__init__(length, width)

    def area_sqr(self):
        return self.length * self.width


class Cube(Area):
    def __init__(self, length, width, height):
        super(Cube, self).__init__(length, width)
        self.height = height

    def area_Cube(self):
        return self.width * self.length * self.height


obj_sqr = Square(3, 4)
print("Area of square : ", obj_sqr.area_sqr())

obj_cube = Cube(3, 4, 5)
print("Area of cube : ", obj_cube.area_Cube())
