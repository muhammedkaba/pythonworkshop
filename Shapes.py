import math
class Shape:
    def __init__(self,name,color,line_type,thickness):
        self.name = name
        self.color = color
        self.line_type = line_type
        self.thickness = thickness
    def get_name(self):
        return self.name
    def set_name(self,s):
        self.name = s
    def get_color(self):
        return self.color
    def set_color(self,c):
        self.color = c
    def get_line_type(self):
        return self.line_type
    def set_line_type(self,l):
        self.line_type = l
    def get_thickness(self):
        return self.thickness
    def set_thickness(self,t):
        self.thickness = t
    def __str__(self):
        print("Name="+self.name)
        print("Color="+self.color)
        print("Line type="+self.line_type)
        return("Thickness="+str(self.thickness))
    def strforothers(self):
        print("Name="+self.name)
        print("Color="+self.color)
        print("Line type="+self.line_type)
        print("Thickness="+str(self.thickness))
        
class Rectangle(Shape):
    def __init__(self,width,height,*args,**kwargs):
        self.width = width
        self.height = height
        super(Rectangle, self).__init__(*args,**kwargs)
    def get_width(self):
        return self.width
    def set_width(self,w):
        self.width = w
    def get_height(self):
        return self.height
    def set_height(self,h):
        self.height = h
    def get_area(self):
        ar = self.width*self.height
        self.area = '{0:.2f}'.format(ar)
        return self.area
    def get_perimeter(self):
        per = 2*(self.width+self.height)
        self.perimeter = '{0:.2f}'.format(per)
        return self.perimeter
    def __str__(self):
        super().strforothers()
        print("Width="+str(self.width))
        print("Height="+str(self.height))
        print("Area="+self.get_area())
        return("Perimeter="+self.get_perimeter())
        
class Circle(Shape):
    def __init__(self,radius,*args,**kwargs):
        self.radius = radius
        super(Circle, self).__init__(*args,**kwargs)
    def get_radius(self):
        return self.radius
    def set_radius(self,r):
        self.radius = r
    def get_area(self):
        ar = ((self.radius**2)*math.pi)
        self.area = '{0:.2f}'.format(ar)
        return self.area
    def get_perimeter(self):
        per = (self.radius)*2*math.pi
        self.perimeter = '{0:.2f}'.format(per)
        return self.perimeter
    def __str__(self):
        super().strforothers()
        print("Radius="+str(self.radius))
        print("Area="+self.get_area())
        return("Perimeter="+self.get_perimeter())
        
class Triangle(Shape):
    def __init__(self,edge1,edge2,edge3,*args,**kwargs):
        self.edge1 = edge1
        self.edge2 = edge2
        self.edge3 = edge3
        super(Triangle, self).__init__(*args,**kwargs)
    def get_edge1(self):
        return self.edge1
    def set_edge1(self,e1):
        self.edge1 = e1
    def get_edge2(self):
        return self.edge2
    def set_edge2(self,e2):
        self.edge2 = e2
    def get_edge3(self):
        return self.edge3
    def set_edge3(self,e3):
        self.edge3 = e3
    def get_area(self):
        u = (self.edge1+self.edge2+self.edge3)/2
        ar = math.sqrt(u*(u-self.edge1)*(u-self.edge2)*(u-self.edge3))
        self.area = '{0:.2f}'.format(ar)
        return self.area
    def get_perimeter(self):
        per = self.edge1+self.edge2+self.edge3
        self.perimeter= '{0:.2f}'.format(per)
        return self.perimeter
    def __str__(self):
        super().strforothers()
        print("Edge1="+str(self.edge1))
        print("Edge2="+str(self.edge2))
        print("Edge3="+str(self.edge3))
        print("Area="+self.get_area())
        return("Perimeter="+self.get_perimeter())
class Square(Shape):
    def __init__(self,edge,*args,**kwargs):
        self.edge = edge
        super(Square, self).__init__(*args,**kwargs)
    def get_edge(self):
        return self.edge
    def set_edge(self,e):
        self.edge = e
    def get_area(self):
        ar = self.edge**2
        self.area = '{0:.2f}'.format(ar)
        return self.area
    def get_perimeter(self):
        per = self.edge*4
        self.perimeter = '{0:.2f}'.format(per)
        return self.perimeter
    def __str__(self):
        super().strforothers()
        print("Edge="+str(self.edge))
        print("Area="+self.get_area())
        return("Perimeter="+self.get_perimeter())