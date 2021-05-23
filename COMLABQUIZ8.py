import math


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area_rect(self):
        a = (self.width * self.height)
        return float(a)

    def get_perimeter_rect(self):
        a = 2*(self.width + self.height)
        return float(a)

    def __str__(self):
        return "\nWidth=" + str(self.width) + "\nHeight=" + str(self.height) + "\nArea=" + "{0:.2f}".format(self.get_area_rect()) + "\nPerimeter=" + "{0:.2f}".format(self.get_perimeter_rect())


class Triangle:
    def __init__(self, edge):
        self.edge = edge

    def get_area_tri(self):
        a = ((self.edge**2) * (math.sqrt(3)/4))
        return float(a)

    def get_perimeter_tri(self):
        a = (3*self.edge)
        return float(a)

    def __str__(self):
        return "\nEdge=" + str(self.edge) + "\nArea=" + "{0:.2f}".format(self.get_area_tri()) + "\nPerimeter=" + "{0:.2f}".format(self.get_perimeter_tri())


class Square(Rectangle):
    def __init__(self, edge):
        super(Square, self).__init__(width=edge, height=edge)


class TrianglePrism(Rectangle, Triangle):
    def __init__(self, edge, height):
        Rectangle.__init__(self, width=edge, height=height)
        Triangle.__init__(self, edge=edge)

    def get_volume(self):
        a = ((self.edge ** 2) * (math.sqrt(3) / 4))*self.height
        return float(a)

    def get_area(self):
        a = (2*float(self.get_area_tri())) + (3*float(self.get_area_rect()))
        return float(a)

    def __str__(self):
        return "\nArea=" + "{0:.2f}".format(self.get_area()) + "\nVolume="+"{0:.2f}".format(self.get_volume())


class SquarePyramid(Square, Triangle):
    def __init__(self, edge):
        Square.__init__(self, edge=edge)
        Triangle.__init__(self, edge=edge)

    def get_area(self):
        a = float(self.get_area_rect()) + (3*float(self.get_area_tri()))
        return float(a)

    def __str__(self):
        return "\nArea=" + "{0:.2f}".format(self.get_area())
